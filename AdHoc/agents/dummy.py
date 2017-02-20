import sys
import random

from .agent import Agent

class Dummy(Agent):

    def __init__(self, seed, port,serverPath = "/home/leno/HFO/bin/"):
        super(Dummy, self).__init__(seed=seed, port=port,serverPath=serverPath)


    def select_action(self,stateFeatures, state):
        """ When this method is called, the agent executes an action. """
        
        
        if stateFeatures[5] == 1: # State[5] is 1 when the player can kick the ball
            #return random.choice([SHOOT, PASS(team_mate), DRIBBLE])
            return random.choice([self.DRIBBLE,self.DRIBBLE, self.SHOOT,self.SHOOT, self.PASSfar, self.PASSnear])
            #return random.choice([self.SHOOT])
            
        return self.MOVE
    def advise_action(self,uNum,state):
        """Verifies if the agent can advice a friend, and return the action if possible"""
        return None #No advising


    def observe_reward(self,state,action,reward,statePrime):
        """ After executing an action, the agent is informed about the state-reward-state tuple """
        pass
    def setupAdvising(self,agentIndex,allAgents):
        """ This method is called in preparation for advising """
        pass
    def step(self, state, action):
        """ Perform a training step """
        #Execute the action in the environment
        self.execute_action(action)
        # Advance the environment and get the game status
        status = self.hfo.step()
        statePrime = self.get_transformed_features(self.hfo.getState())
        actionPrime = self.select_action(self.hfo.getState(), statePrime)
        return status, statePrime, actionPrime
