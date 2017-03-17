# -*- coding: utf-8 -*-
"""
File that stores the learning results

@author: Felipe Leno
"""

from sarsatile import SARSATile
class SARSATileStorage(SARSATile):

   storagePath = None
   visitTable = None
   qTableFile = 'QTable.txt'
   visitFile = 'VisitTable.txt'
    
   def __init__(self, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345, port=12345, 
                lowerBoundVariables=-1, upperBoundVariables=+1, tilesNumber=10,tileWidth=0.5,serverPath = "/home/leno/HFO/bin/",
                storagePath="agentData/"):
         super(SARSATileStorage, self).__init__(epsilon=epsilon, alpha=alpha, gamma=gamma, 
            decayRate=decayRate,seed=seed, port=port, serverPath=serverPath)          
         self.storagePath = storagePath
         self.visitTable = {}

   def finish_training(self):
       fileToWrite = self.storagePath + self.qTableFile
       
       import cPickle
       #Stores the Q-table for posterior reuse
       with open(fileToWrite,"wb") as qFile:
           cPickle.dump(self.qTable, qFile)
       #Stores number of visits per state
       fileToWrite = self.storagePath + self.visitFile
       with open(fileToWrite,"wb") as qFile:
           cPickle.dump(self.visitTable, qFile)
       
       
   def step(self, state, action):
        """Modifies the default step action just to include a state visit counter"""
        if self.exploring:
                processedState = self.quantize_features(state)
                self.visitTable[processedState] = self.visitTable.get(processedState,0.0) + 1
        return super(SARSATileStorage, self).step(state,action)
