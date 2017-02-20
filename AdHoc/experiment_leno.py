# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 17:29:45 2016

@author:Felipe Leno

Before running this program, first Start HFO server:
$> ./bin/HFO --offense-agents 1

This File executes the experiment. The first argument is the agent name, which will be used to load the correct
agent implementation. 

The experiment is carried out as follows: 

A training episode is executed <nIntervalEvaluation> times. After that, the agent exploration is turned off and <nEvaluations> episodes are executed
to evaluate the algorithm performance. This procedure is repeated until the number of training trials is exceeded

"""

#!/usr/bin/env python
# encoding: utf-8

# Before running this program, first Start HFO server:
# $> ./bin/HFO --offense-agents 1

import random, itertools
from hfo import *

def runExperiment(argv):
    """Executes the Experiment Main Loop, this method calls the agent initialization, process rewards,
       and calculates the metrics
    """
    #Some random parameter values for initial tests
    nIntervalEvaluation = 5
    nEvaluations = 5
    
    # Create the HFO Environment
    hfo = HFOEnvironment()
    # Connect to the server with the specified
    # feature set. See feature sets in hfo.py/hfo.hpp.
    hfo.connectToServer(HIGH_LEVEL_FEATURE_SET,
                      '/bin/teams/base/config/formations-dt', 6000,
                      'localhost', 'base_left', False)
                      
    # A subclass of Agent must be returned by this method.
    agent = initiateAgent(argv, hfo);
 
    #Loop Executed for each learning episode
    for episode in itertools.count():
        curState = hfo.getState()
        
        #----Training episode----
        status = IN_GAME
        while status == IN_GAME:
          #The agent applies one action
          agent.act(curState)
          #The game status and reward are defined
          status = hfo.step()
          reward = getReward(status)
          #the new state is observed
          statePrime = hfo.getState()
          #The agent Update is executed
          agent.observeReward(curState,reward,statePrime)
          #The current state is updated
          curState = statePrime
        #------End of Training episode------------  
          
        #Should an evaluation be executed?
        if(episode%nIntervalEvaluation==0):
            #The agent exploration is disabled
            agent.setExploring(False)
            #The evaluation episodes are executed (no Q-value updates)
            allGoals = 0.0
            totalTimeToGoal = 0.0
            for evEpisodes in range(1,nEvaluations):
                steps = 0
                status = IN_GAME
                while status == IN_GAME:
                    state = hfo.getState()
                    agent.act(state)
                    status = hfo.step()
                    steps = steps+1
                    #Process metrics
                    if(status==GOAL):
                        allGoals = allGoals+1
                        totalTimeToGoal = totalTimeToGoal + steps
                
            #After the evaluation is finished, the metrics are computed and displayed
            print "Goal Percentage: "+ str(allGoals/nEvaluations)
            print "Average Time to Goal: " + str(totalTimeToGoal/allGoals) 
            
            agent.setExploring(True)
           
           
#Check this method
def initiateAgent(argv, hfo):
    """Initiates the correct agent class"""
    try:
        Agent = getattr(
                __import__('agent.' + argv[1].lower(),
                        fromlist=[argv[1]]),argv[1])
    except ImportError:
        sys.stderr.write("ERROR: missing python module: " + argv[1] + "\n")
        sys.exit(1)
    return Agent(hfo, argv, target_dir = target_dir)
        
def getReward(status):
    """The Reward Function returns -1 when a defensive agent captures the ball, 
    +1 when the agent's team scores a goal and 0 otherwise"""
    if(status == CAPTURED_BY_DEFENSE):
         return -1
    elif(status==GOAL):
         return +1
    return 0;

if __name__ == '__main__':
  main(sys.argv[1:])#arguments)
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
