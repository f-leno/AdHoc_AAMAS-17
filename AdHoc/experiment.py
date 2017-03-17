#!/usr/bin/env python
# encoding: utf-8
# Authors: Felipe Leno, Ruben Glatt
# THis program is the main loop of the experiment, the arguments will specify which type of agent will be executed in the HFO server,
# all experiments were executed using this code with different parameters.
#
# Before running this program, first Start HFO server:
# $> ./bin/HFO --offense-agents 1

import argparse
import sys
import os
import csv
import random, itertools
from hfo import *
from threading import Thread
from time import sleep
#from cmac import CMAC


from agents.agent import Agent
from statespace_util import *



#Arguments
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--number_agents',type=int, default=3)
    parser.add_argument('-a1','--agent1',  default='Dummy')
    parser.add_argument('-a2','--agent2',  default='Dummy')
    parser.add_argument('-a3','--agent3',  default='Dummy')
    parser.add_argument('-a4','--agent4',  default='Dummy')
    parser.add_argument('-a5','--agent5',  default='Dummy')
    parser.add_argument('-a6','--agent6',  default='Dummy')
    parser.add_argument('-a7','--agent7',  default='Dummy')
    parser.add_argument('-a8','--agent8',  default='Dummy')
    parser.add_argument('-a9','--agent9',  default='Dummy')
    parser.add_argument('-a10','--agent10',default='Dummy')
    parser.add_argument('-a11','--agent11',default='Dummy')
    parser.add_argument('-t','--learning_trials',type=int, default=10)
    parser.add_argument('-i','--evaluation_interval',type=int, default=5)
    parser.add_argument('-d','--evaluation_duration',type=int, default=5)
    parser.add_argument('-s','--seed',type=int, default=12345)
    parser.add_argument('-l','--log_file',default='../log/')
    parser.add_argument('-p','--port',type=int, default=12345)
    parser.add_argument('-r','--number_trial',type=int, default=1)
    parser.add_argument('-e','--server_path',  default='../HFO/bin/')
    return parser.parse_args()


def build_agents():
    """Builds and returns the agent objects as specified by the arguments"""
    agents = []    
    
    
    parameter = get_args()
    
    for i in range(parameter.number_agents):
        agentName = getattr(parameter,"agent"+str(i+1))
        print "AgentName: "+agentName
        try:
           AgentClass = getattr(
                __import__('agents.' + (agentName).lower(),
                        fromlist=[agentName]),
                agentName)
        except ImportError:
           sys.stderr.write("ERROR: missing python module: " +agentName + "\n")
           sys.exit(1)
    
        print "Creating agent"
        AGENT = AgentClass(seed=parameter.seed, port=parameter.port, serverPath = parameter.server_path)
        print "OK Agent"
        agents.append(AGENT)
        
    return agents
    

def main():
    parameter = get_args()
    print parameter
    print('***** Loading agent implementations')
    agents = build_agents()
    print('***** %s: Agents online --> %s')
    print "Agent Classes OK"
    #Initiate agent Threads    
    global okThread
    okThread = True
    
    
    #As we need more than one agent in the team, separated threads execute
    #each needed agent
    agentThreads = []
    
    try:
        #Initiating agent
        for i in range(parameter.number_agents):
            agentThreads.append(Thread(target = thread_agent, args=(agents[i],agents,i,parameter)))
            agentThreads[i].start()
            sleep(4)
            
            
        #Waiting for program termination
        for i in range(parameter.number_agents):
            agentThreads[i].join()
            
    except Exception as e:
        print e.__doc__
        print e.message
        okThread = False
   
    

    

    
    
def thread_agent(agentObj,allAgents,agentIndex,mainParameters):
    """This method is executed by each thread in the system and corresponds to the control
    of one playing agent"""
    
    logFolder = mainParameters.log_file + getattr(mainParameters,"agent"+str(agentIndex+1))
    if not os.path.exists(logFolder):
                os.makedirs(logFolder)
    logFolder += "/_0_"+str(mainParameters.number_trial)+"_AGENT_"+str(agentIndex+1)+"_RESULTS"
    
    #Connecting agent to server 
    print "******Connecting agent "+str(agentIndex)+"****"
    agentObj.connectHFO()
    #Building Log folder name
    print "******Connected agent "+str(agentIndex)+"****"
    
   
    train_csv_file = open(logFolder + "_train", "wb")
    train_csv_writer = csv.writer(train_csv_file)
    train_csv_writer.writerow(("trial","frames_trial","goals_trial","used_budget"))
    train_csv_file.flush()
    print('***** %s: Setting up eval log files' % str(agentObj.unum))
    #eval_csv_file = open(parameter.log_file + "_" + str(AGENT.unum) + "_eval", "wb")
    eval_csv_file = open(logFolder + "_eval", "wb")
    eval_csv_writer = csv.writer(eval_csv_file)
    eval_csv_writer.writerow(("trial","goal_percentage","avg_goal_time","used_budget","disc_reward"))
    eval_csv_file.flush()
    
    #Setups advising
    agentObj.setupAdvising(agentIndex,allAgents)
    gamma=agentObj.gamma

    print('***** %s: Start training' % str(agentObj.unum))
    for trial in range(0,mainParameters.learning_trials+1):
        # perform an evaluation trial
        if(trial % mainParameters.evaluation_interval == 0):
            #print('***** %s: Running evaluation trials' % str(AGENT.unum) )
            agentObj.set_exploring(False)
            goals = 0.0
            time_to_goal = 0.0         
            discR = 0.0
            for eval_trials in range(1,mainParameters.evaluation_duration+1):
                eval_frame = 0
                curGamma = 1.0
                eval_status = agentObj.IN_GAME
                stateFeatures = agentObj.hfo.getState()
                state = agentObj.get_transformed_features(stateFeatures)
                #action = AGENT.select_action(tuple(stateFeatures), state)
                action = agentObj.select_action(stateFeatures, state, False)
                while eval_status == agentObj.IN_GAME:
                    eval_frame += 1
                    eval_status, state, action = agentObj.step(state, action)
                    discR = discR + agentObj.get_reward(eval_status) * curGamma
                    curGamma = curGamma * gamma
                    if(eval_status == agentObj.GOAL):
                        goals += 1.0
                        time_to_goal += eval_frame
                        #print('********** %s: GGGGOOOOOOOOOOLLLL: %s in %s' % (str(AGENT.unum), str(goals), str(time_to_goal)))
            goal_percentage = 100*goals/mainParameters.evaluation_duration
            #print('***** %s: Goal Percentage: %s' % (str(AGENT.unum), str(goal_percentage)))
            if (goals != 0):
                avg_goal_time = time_to_goal/goals
            else:
                avg_goal_time = 0.0
            #print('***** %s: Average Time to Goal: %s' % (str(AGENT.unum), str(avg_goal_time)))
            # save stuff
            eval_csv_writer.writerow((trial,"{:.2f}".format(goal_percentage),"{:.2f}".format(avg_goal_time),str(agentObj.get_used_budget()),"{:.10f}".format(discR)))
            eval_csv_file.flush()
            agentObj.set_exploring(True)
            # reset agent trace
            agentObj.stateActionTrace = {} 
           
        
        #print('***** %s: Starting Learning Trial %d' % (str(AGENT.unum),trial))
        status = agentObj.IN_GAME
        frame = 0
        stateFeatures = agentObj.hfo.getState()
        state = agentObj.get_transformed_features(stateFeatures)
        #print('***** %s: state type: %s, len: %s' % (str(AGENT.unum), str(type(state)), str(len(state))))
        #action = AGENT.select_action(tuple(stateFeatures), state)
        action = agentObj.select_action(stateFeatures, state, False)
        #print "Selected action --- "+str(action)
        while status == agentObj.IN_GAME:
            frame += 1
            status, state, action = agentObj.step(state, action)
        #print('***** %s: Trial ended with %s'% (str(AGENT.unum), AGENT.hfo.statusToString(status)))
        #print('***** %s: Agent --> %s'% (str(AGENT.unum), str(AGENT)))
        reward = agentObj.get_reward(status)
        # save stuff
        train_csv_writer.writerow((trial,frame,reward,str(agentObj.get_used_budget())))
        train_csv_file.flush()
        agentObj.stateActionTrace = {}



        # Quit if the server goes down
        if status == agentObj.SERVER_DOWN:
            agentObj.hfo.act(QUIT)
            print('***** %s: Shutting down agent' % str(agentObj.unum))
            break
    print('***** %s: Agent --> %s'% (str(agentObj.unum), str(agentObj)))
    eval_csv_file.close()
    train_csv_writer.writerow(("-","-",str(agentObj)))
    train_csv_file.flush()
    train_csv_file.close()
    agentObj.hfo.act(QUIT)
    agentObj.finish_training()

if __name__ == '__main__':
    main()
