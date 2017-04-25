# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:21:38 2016

@author: Felipe Leno

This file implements our ad hoc advising proposal.

This agent act as SARSA, and the exploration strategy is changed according to our proposal
"""

from sarsatile import SARSATile
from threading import Thread
from advice_util import AdviceUtil
import random
from time import sleep
import math
import agent

import abc

class AdHoc(SARSATile):
    startAdvice = None
    learningEpisodes = None 
    budgetAsk = 0
    budgetAdvise = 0
    spentBudgetAsk = 0
    spentBudgetAdvise = 0
    
    scalingVisits = math.exp(10)
    
    lastStatus = agent.IN_GAME
    
    #Enum for importance metrics
    VISIT_IMPORTANCE, Q_IMPORTANCE = range(2)
    
    stateImportanceMetric = None
    
    adviceObject = None
    
    ASK,ADVISE = range(2)
    visitTable = None
    
    advisedState = None
    informAction = None #must be informed in subclass    
    
    
    def __init__(self, budgetAsk, budgetAdvise,stateImportanceMetric,seed=12345, port=12345,epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/"):
        super(AdHoc, self).__init__(seed=seed,port=port,serverPath = serverPath)
        self.name = "AdHoc"
        self.visitTable = {}
        self.advisedState = {}
        self.budgetAsk = budgetAsk
        self.budgetAdvise = budgetAdvise        
        self.stateImportanceMetric = stateImportanceMetric
        self.startAdvice = 1
        self.learningEpisodes = 0 
        
    def select_action(self, stateFeatures, state, noAdvice=False):
        """Changes the exploration strategy"""
        if self.exploring and self.spentBudgetAsk < self.budgetAsk and stateFeatures[self.ABLE_KICK] == 1 and not noAdvice and self.learningEpisodes >= self.startAdvice:
            #Check if it should ask for advice
            ask = self.check_ask(state)
            if ask:
                #----
                #Ask for advice
                #----
            
                #In case the agent will communicate its intended action
                if self.informAction:
                    normalAction = super(AdHoc, self).select_action(stateFeatures,state)
                else:
                    normalAction = None                    
            
                advised = self.adviceObject.ask_advice(self.get_Unum(),stateFeatures,normalAction)
                
                if advised:
                    try:
                        self.advisedState[self.quantize_features(state)] = True
                        self.spentBudgetAsk = self.spentBudgetAsk + 1
                        action = self.combineAdvice(advised)
                        return action
                    except:
                        print "Exception when combining the advice " + str(advised)
                #No need to compute two times the intended action
                if self.informAction:
                    return normalAction
                    
        return super(AdHoc, self).select_action(stateFeatures,state,noAdvice)
      
    @abc.abstractmethod
    def check_advise(self,stateFeatures,state): 
        """Returns if the agent should advice in this state.
        The advised action is also returned in the positive case"""
            
        
    def combineAdvice(self,advised):
        return int(max(set(advised), key=advised.count))
        
    def state_importance(self,state,typeProb):
        """Calculates the state importance
        state - the state
        typeProb - is the state importance being calculated in regard to
        the number of visits or also by Q-table values?"""
        processedState = self.quantize_features(state)
        numberVisits = self.number_visits(processedState)
         
        
        if numberVisits == 0:
            return 0.0
            
        visitImportance = numberVisits / (numberVisits + math.log(self.scalingVisits + numberVisits))
        
        if typeProb == self.VISIT_IMPORTANCE:
            return visitImportance
        elif typeProb==self.Q_IMPORTANCE:            
            
            maxQ = -float("inf")
            minQ = float("inf")
            #Get max and min Q value
            actions = [self.DRIBBLE, self.SHOOT, self.PASSfar, self.PASSnear]
            for act in actions:
                if (processedState,act) in self.qTable:
                    actQ = self.qTable.get((processedState, act))
                    if actQ > maxQ:
                        maxQ = actQ
                    if actQ < minQ:
                        minQ = actQ
            
            # print "MaxQ "+str(maxQ)
            # print "MinQ "+str(minQ)
            # print "len "+str(len(actions))
            qImportance = math.fabs(maxQ - minQ) #* len(actions)
            if qImportance==float('inf'):
                return 0.0
            #if qImportance != 0:
                #print str(qImportance) + " - "+str(visitImportance)
            return   qImportance / (1-visitImportance)       
        #If the agent got here, it is an error
        return None
        
    def step(self, state, action):
        """Modifies the default step action just to include a state visit counter"""
        if self.exploring:
                processedState = self.quantize_features(state)
                self.visitTable[processedState] = self.visitTable.get(processedState,0.0) + 1
        status, statePrime, actionPrime = super(AdHoc, self).step(state,action)
        self.lastStatus = status
        
        if self.lastStatus != self.IN_GAME:
            self.advisedState = {}
            if self.exploring:
                self.learningEpisodes += 1
        
        return status, statePrime, actionPrime
        
    @abc.abstractmethod    
    def check_ask(self,state):
        """Returns if the agent should ask for advise in this state"""
        
 
        
    def calc_prob_adv(self,importance,midpoint,typeProb):
        """Calculates the probability of giving/receiving advice
        importance - the current state importance
        midpoint - the midpoint for the logistic function
        typeProb - ASK or ADVISE
        """
        signal = 1 if typeProb == self.ASK else -1
        k = 10    
        
        prob = 1 / (1 + math.exp(signal * k * (importance-midpoint)))
        return prob
        
    def advise_action(self,uNum,state,adviseeAction=None):
        """Verifies if the agent can advice a friend, and return the action if possible"""
        if self.spentBudgetAdvise < self.budgetAdvise:
            #Check if the agent should advise
            advise,advisedAction = self.check_advise(state,self.get_transformed_features(state))
            if advise:
                if adviseeAction is None or advisedAction!=adviseeAction:
                    self.spentBudgetAdvise = self.spentBudgetAdvise + 1
                    return advisedAction
        return None
        
    
    def setupAdvising(self,agentIndex,allAgents):
        """ This method is called in preparation for advising """
        self.adviceObject = AdviceUtil()
        advisors = [x for i,x in enumerate(allAgents) if i!=agentIndex]
        self.adviceObject.setupAdvisors(advisors)

        
                                
                    
    def get_used_budget(self):
        return self.spentBudgetAdvise
    @abc.abstractmethod
    def midpoint(self,typeMid):
        """Calculates the midpoint"""
        pass
        
        
    def number_visits(self,state):
        return self.visitTable.get(state,0.0)