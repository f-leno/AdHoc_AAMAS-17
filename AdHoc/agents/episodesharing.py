# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:26:56 2016

Implementation of Episode Sharing
@author: Felipe Leno
"""

from sarsatile import SARSATile

class EpisodeSharing(SARSATile):
    
    fellowAgents = None
    spentBudget = None
    budget = None
    episodeUpdateTrace = None
    def __init__(self, budget=1000, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345, port=12345, 
                lowerBoundVariables=-1, upperBoundVariables=+1, tilesNumber=10,tileWidth=0.5,serverPath = "/home/leno/HFO/bin/"):
         super(EpisodeSharing, self).__init__(epsilon=epsilon, alpha=alpha, gamma=gamma, 
            decayRate=decayRate,seed=seed, port=port, serverPath=serverPath)           
         self.budget = budget
         self.spentBudget = 0
         self.fellowAgents = []
         self.episodeUpdateTrace = []
    
    
    def setupAdvising(self,agentIndex,allAgents):
        """ This method is called in preparation for advising """
        fellows = [x for i,x in enumerate(allAgents) if i!=agentIndex]
        self.fellowAgents = fellows
        
    def get_used_budget(self):
        return self.spentBudget
        
    def adviseFellow(self):
        """Perform the episode sharing"""
        useTrace = {}
        if self.spentBudget < self.budget:
            for i in range(len(self.episodeUpdateTrace)):
                state = self.episodeUpdateTrace[i][0]
                action = self.episodeUpdateTrace[i][1]
                statePrime = self.episodeUpdateTrace[i][2]
                statePrimeFeatures = self.episodeUpdateTrace[i][3]
                reward = self.episodeUpdateTrace[i][4]
                stateAction = self.episodeUpdateTrace[i][5]
                
                
                useTrace[(state, action)] = useTrace.get((state, action), 0) + 1
                for agent in self.fellowAgents:
                    if self.spentBudget < self.budget:
                        agent.updateFromAdvice(state,action,statePrime,statePrimeFeatures,reward,stateAction,useTrace)
                        self.spentBudget = self.spentBudget + 1
                for stateAction in useTrace:
                        useTrace[stateAction] = self.gamma * self.decayRate * useTrace.get(stateAction, 0)
                        
                        
                                

    
    def updateFromAdvice(self,state,action,statePrime,statePrimeFeatures,reward,stateAction,trace):
        """Updates Q table from advice""" 
        actionPrime = self.select_action(statePrimeFeatures, statePrime)
        TDError = reward + self.gamma * self.get_Q(statePrime, actionPrime) - self.get_Q(state, action)
        for stateAction in trace:
                # update update ALL Q values and eligibility trace values
                self.qTable[stateAction] = self.qTable.get(stateAction, 0) + TDError * self.alpha * trace.get(stateAction, 0)

                
    def step(self, state, action):
        """ Perform a complete training step """
        # perform action and observe reward & statePrime
        self.execute_action(action)
        status = self.hfo.step()
        stateFeatures = self.hfo.getState()
        statePrime = self.get_transformed_features(stateFeatures)
        stateQuantized = self.quantize_features(state)
        statePrimeQuantized = self.quantize_features(statePrime)
        reward = self.get_reward(status)
        # select actionPrime
        actionPrime = self.select_action(stateFeatures, statePrime)

        if self.exploring:
            # calculate TDError
            TDError = reward + self.gamma * self.get_Q(statePrimeQuantized, actionPrime) - self.get_Q(stateQuantized, action)

            # update trace value
            self.stateActionTrace[(stateQuantized, action)] = self.stateActionTrace.get((stateQuantized, action), 0) + 1
            
                        #Will be used for advice                
            self.episodeUpdateTrace.append((stateQuantized,action,statePrimeQuantized,statePrime,reward,(stateQuantized, action),self.stateActionTrace.get((stateQuantized, action), 0)))
            
            for stateAction in self.stateActionTrace:
                # update update ALL Q values and eligibility trace values
                self.qTable[stateAction] = self.qTable.get(stateAction, 0) + TDError * self.alpha * self.stateActionTrace.get(stateAction, 0)

                # update eligibility trace Function for state and action
                self.stateActionTrace[stateAction] = self.gamma * self.decayRate * self.stateActionTrace.get(stateAction, 0)
            #self.learn(stateQuantized, action, reward,
            #           statePrimeQuantized, actionPrime)
            self.training_steps_total += 1
        if status == self.GOAL:
            self.adviseFellow()
        if status != self.IN_GAME:
            self.stateActionTrace = {}
            self.episodeUpdateTrace = []
        return status, statePrime, actionPrime