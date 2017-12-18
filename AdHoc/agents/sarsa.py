import sys
import random

from .agent import Agent

#from cmac import CMAC

class SARSA(Agent):

    def __str__(self):
        """ Overwrites the object.__str__ method.

        Returns:
            string (str): Important parameters of the object.
        """
        return "Agent: " + str(self.unum) + ", " + \
               "Type: " + str(self.name) + ", " + \
               "Training steps: " + str(self.training_steps_total) + ", " + \
               "Q-Table size: " + str(len(self.qTable))

    def __init__(self, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345,
                 cmac_level=20, cmac_quantization=0.3, cmac_beta=0.1, port=12345,serverPath = "../HFO/bin/"):
        super(SARSA, self).__init__(seed, port,serverPath=serverPath)
        self.name = "SARSA"
        self.qTable = {}
        self.stateActionTrace = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.decayRate = decayRate
	#the cmac attribute is assigned at SARSATile
        #self.cmac = CMAC(cmac_level,cmac_quantization,cmac_beta) 
        #print('***** %s: Agent uses CMAC(%s,%s,%s)' % (str(self.unum),str(cmac_level), str(cmac_quantization), str(cmac_beta)))

    def quantize_features(self, features):
        """ CMAC utilities for all agent """
        quantVar = self.cmac.quantize(features)        
  #      data = []
        data = quantVar
        #len(quantVar[0]) is the number of variables
#        for i in range(0,len(quantVar[0])):
            #Transforms n tuples into a single array
#            for var in quantVar:
                #copy each tuple value to the output
#                data.append(var[i])
        #returns the output as a tuple
        return tuple(data)

    def advise_action(self,uNum,state):
        """Verifies if the agent can advice a friend, and return the action if possible"""
        return None #No advising

    def get_Q(self, state, action):
        return self.qTable.get((state, action), 0.0)

    def observe_reward(self,state,action,reward,statePrime):
        """ After executing an action, the agent is informed about the state-reward-state tuple """
        pass


    def select_action(self, stateFeatures, state, noAdvice=False):
        """Executes the epsilon-greedy exploration strategy"""
        #stores last CMAC result
        #self.lastState = state
        # select applicable actions
        if stateFeatures[5] == 1: # State[5] is 1 when the player can kick the ball
            actions = [self.SHOOT, self.DRIBBLE, self.PASSfar, self.PASSnear]
        else:
            return self.MOVE
        # epsilon greedy action selection
        if self.exploring and random.random() < self.epsilon and not noAdvice:
            actionsRandom = [ self.SHOOT,self.DRIBBLE, self.DRIBBLE, self.SHOOT, self.PASSfar, self.PASSnear]
            return random.choice(actionsRandom)
        else:
            cmacState = self.quantize_features(state)
            qValues = [self.get_Q(cmacState, action) for action in actions]
            maxQ = max(qValues)
            count = qValues.count(maxQ)
            if count > 1: #and self.exploring:
                best = [i for i in range(len(actions)) if qValues[i] == maxQ]
                if not self.exploring:
                    return actions[best[0]]
                return actions[random.choice(best)]
            else:
                return actions[qValues.index(maxQ)]


    def learn(self, state1, action1, reward, state2, action2):
        qnext = self.get_Q(state2, action2)
        self.learn_Q(state1, action1, reward, reward + self.gamma * qnext)

    def learn_Q(self, state, action, reward, value):
        oldv = self.qTable.get((state, action), None)
        if oldv is None:
            self.qTable[(state, action)] = reward
        else:
            self.qTable[(state, action)] = oldv + self.alpha * (value - oldv)

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
        if self.exploring:
            actionPrime = self.select_action(stateFeatures, statePrime,False)
        else:
            actionPrime = self.select_action(stateFeatures, statePrime,True)

        if self.exploring:
            # calculate TDError
            TDError = reward + self.gamma * self.get_Q(statePrimeQuantized, actionPrime) - self.get_Q(stateQuantized, action)
            # update trace value
            self.stateActionTrace[(stateQuantized, action)] = self.stateActionTrace.get((stateQuantized, action), 0) + 1
            for stateAction in self.stateActionTrace:
                # update update ALL Q values and eligibility trace values
                self.qTable[stateAction] = self.qTable.get(stateAction, 0) + TDError * self.alpha * self.stateActionTrace.get(stateAction, 0)
                # update eligibility trace Function for state and action
                self.stateActionTrace[stateAction] = self.gamma * self.decayRate * self.stateActionTrace.get(stateAction, 0)
            #self.learn(stateQuantized, action, reward,
            #           statePrimeQuantized, actionPrime)
            self.training_steps_total += 1
        if status != self.IN_GAME:
            self.stateActionTrace = {}
        return status, statePrime, actionPrime
    def setupAdvising(self,agentIndex,allAgents):
        """ This method is called in preparation for advising """
        pass
