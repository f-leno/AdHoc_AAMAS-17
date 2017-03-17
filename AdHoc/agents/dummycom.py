# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:45:44 2016

@author: Felipe Leno

Test for communicating agents. The hear and say methods provided by HFO
don't work for python agents (at least by the time this experiment is implemented).

This agent communicates through text files. Of course this only works if all agents are executed in the same pc.
TODO: an actual message passing implementation
"""



import random
import advice_util as advice 

from agent import Agent
from threading import Thread

class DummyCom(Agent):

   
    steps = 0
    spentBudget = 0
    budget = 10


    def __init__(self):
        super(DummyCom, self).__init__()
        #The agent runs a separated thread for advising
        thread = Thread(target = self.advise)#, args = (self, ))
        thread.start()
        
        


    def select_action(self,state):
        """ When this method is called, the agent executes an action. """
        if self.exploring:
            advised = advice.ask_advice(self.get_Unum(),state)
            if advised:
                print "ADVISED: "+''.join(str(e) for e in advised)

            
            

            self.steps = self.steps+1


        if state[5] == 1: # State[5] is 1 when the player can kick the ball
            #return random.choice([SHOOT, PASS(team_mate), DRIBBLE])
            return random.choice([self.DRIBBLE, self.SHOOT])
        return self.MOVE


    def observe_reward(self,state,action,reward,statePrime):
        """ After executing an action, the agent is informed about the state-reward-state tuple """
        pass
    
        
    def step(self, state, action):
        """ Perform a training step """
        #Execute the action in the environment
        self.execute_action(action)
        # Advance the environment and get the game status
        status = self.hfo.step()
        statePrime = self.get_transformed_features(self.hfo.getState())
        
        actionPrime = self.select_action(statePrime)
        return status, statePrime, actionPrime

    def advise(self):
        while self.spentBudget < self.budget:
            reads = advice.verify_advice(self.get_Unum())            

            if reads:
                print reads
            for ad in reads:
                advisee = ad[0]
                state = ad[1]
                if state != "":
                    advice.give_advice(advisee,self.get_Unum(),self.get_Unum())
                    self.spentBudget = self.spentBudget + 1
                    print str(self.spentBudget)
   
