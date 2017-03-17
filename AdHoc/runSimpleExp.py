# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:59:59 2016

@author: leno
"""
import subprocess
import sys
import math
from threading import Thread
import argparse

from time import sleep
import time

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--result_path', default = "/home/leno/HFO/log/")
    parser.add_argument('-n','--number_agents',type=int, default=3)
    parser.add_argument('-a','--agent_class',  default='Dummy')
    parser.add_argument('-e','--server_path',  default='/home/leno/HFO/bin/')
    parser.add_argument('-o','--opponents',  type=int, default=1)
    parser.add_argument('-t','--learning_trials',type=int, default=500)
    parser.add_argument('-i','--evaluation_interval',type=int, default=10)
    parser.add_argument('-d','--evaluation_duration',type=int, default=50)
    parser.add_argument('-r','--number_of_trials' ,type=int, default=1)
    parser.add_argument('-s','--seed',type=int, default=12345)
    parser.add_argument('-p','--port',type=int, default=12345)
    return parser.parse_args()

def main():

    parameter = get_args()
    numberRuns = parameter.number_of_trials
    agent = parameter.agent_class
    n=0
    start_time = time.time()
    while n<numberRuns:
        #subprocess.call("killall -9 rcssserver",shell='True')
        sleep(3)
        run_time = time.time()
        ok = runExp(n+1,agent,parameter)
        if ok:
            n = n+1
            print "Run "+str(n)+" OK Run Time: " + str(time.time() - run_time) 

    print "End of Experiment -- Total Time: "+ str(time.time()- start_time)



def thread_server(command): 
    global okThread
    f = open("/home/leno/HFO/log/Dummy/logserver.txt","w")

    try:
        print "Starting server...."
        okThread = True
        print command
        subprocess.check_call(command,stdout = f, stderr = f, shell='True')

    except subprocess.CalledProcessError as e:
        print "Failed Server... Starting Over"
        #subprocess.call("killall -9 rcssserver",shell='True')
        okThread = False
        print e.__doc__
        print e.message
    f.close()
        
def thread_agent(command): 
    global okThread
    f = open("/home/leno/HFO/log/Dummy/logagent.txt","w")
    try:
        print "Starting Agent...."
        subprocess.check_call(command,stdout = f, stderr = f,shell='True')
    except subprocess.CalledProcessError:
        print "Failed Agent... Starting Over"
        okThread = False
    f.close()
    
   




def runExp(trial,agent,parameter):
    experimentAgentParam = "-n "+str(parameter.number_agents)+" -p "+ str(parameter.port)+" -s "+str(parameter.seed) +  " -i " + str(parameter.evaluation_interval) \
        + " -d "+ str(parameter.evaluation_duration) + " -t "+str(trial)+ " -l "+parameter.result_path + " -e "+ parameter.server_path + " -r "+str(trial)

    
    trialsServer = int(parameter.learning_trials + parameter.evaluation_duration * (parameter.learning_trials / parameter.evaluation_interval + 1)  )
    serverParam = "--offense-agents="+str(parameter.number_agents)+" --defense-npcs="+str(parameter.opponents)+" --fullstate --headless "+\
       "--trials="+str(trialsServer)+ " --port="+str(parameter.port)+" --frames-per-trial=200"
    
    serverScript = parameter.server_path+ "HFO "+ serverParam
    
    
    global okThread
    okThread = False    
    
    while not okThread:
        print serverScript
        threadServer = Thread(target = thread_server, args=(serverScript,))
        threadServer.start()
        sleep(5)

    """ resultPath1 = resultPath + str(trial)+"_AGENT_1_RESULTS"
    agentScript1 = sourcePath + experimentAgentParam + resultPath1 +  " -a "+agent
    threadAgent1 = Thread(target = thread_agent, args=(agentScript1,))
    
    resultPath2 = resultPath + str(trial)+"_AGENT_2_RESULTS"
    agentScript2 = sourcePath + experimentAgentParam + resultPath2 +  " -a "+agent
    threadAgent2 = Thread(target = thread_agent, args=(agentScript2,))
    
    resultPath3 = resultPath + str(trial)+"_AGENT_3_RESULTS"
    agentScript3 = sourcePath + experimentAgentParam + resultPath3 +  " -a "+agent
    threadAgent3 = Thread(target = thread_agent, args=(agentScript3,))"""
        
  
    
    #threadAgent1.start()
    #sleep(5)
    #threadAgent2.start()
    #sleep(5)
    #threadAgent3.start()
    agentParam = experimentAgentParam 
    for i in range(1,parameter.number_agents+1):
        agentParam = agentParam+" -a"+str(i)+" "+agent
        
    okThread = True
    agentCommand = "python experiment.py "+agentParam
    
    threadAgents = Thread(target = thread_agent, args=(agentCommand,))  
    
    threadAgents.start()
    
   
    #Wait for server
    while threadServer.isAlive() and threadAgents.isAlive() and okThread:
        sleep(5)
        #print "Waiting..."
    #threadServer.join()
    #threadAgent1.join()
    #threadAgent2.join()
    #threadAgent3.join()
    #print "OK"
    return okThread 
    
    
    




if __name__ == '__main__':
    main()
    








