# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:31:16 2016
Executes a SARSA Agent Loading the saved Q-table
@author: Felipe Leno
"""

from sarsatile import SARSATile


class SARSATileLoading(SARSATile):
   storagePath = None
   qTableFile = 'QTable.txt'
    
   
   def __init__(self, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345, port=12345, 
                lowerBoundVariables=-1, upperBoundVariables=+1, tilesNumber=10,tileWidth=0.5,serverPath = "/home/leno/HFO/bin/",
                storagePath="agentData/"):
         super(SARSATileLoading, self).__init__(epsilon=epsilon, alpha=alpha, gamma=gamma, 
            decayRate=decayRate,seed=seed, port=port, serverPath=serverPath)          
         self.storagePath = storagePath
         self.load_qtable()
         
   def load_qtable(self):
         fileToWrite = self.storagePath + self.qTableFile
         import cPickle
         with open(fileToWrite, "rb") as myFile:
             self.qTable = cPickle.load(myFile)