# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:22:11 2016
Episode Sharing with successfull episode sharing
@author: Felipe Leno
"""
from episodesharing import EpisodeSharing

class EpisodeSharingLoading(EpisodeSharing):
   storagePath = None
   visitTable = None
   qTableFile = 'QTable.txt'
   visitFile = 'VisitTable.txt'
    
    
   def __init__(self, budget=1000, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345, port=12345, 
                lowerBoundVariables=-1, upperBoundVariables=+1, tilesNumber=10,tileWidth=0.5,serverPath = "/home/leno/HFO/bin/",storagePath="agentData/"):
        super(EpisodeSharingLoading, self).__init__(budget = budget,epsilon=epsilon, alpha=alpha, gamma=gamma, decayRate=decayRate,
                lowerBoundVariables=lowerBoundVariables, upperBoundVariables=upperBoundVariables, tilesNumber=tilesNumber,tileWidth=tileWidth,
                port = port, seed=seed,serverPath = serverPath)
        self.storagePath = storagePath
        self.load_qtable()
        self.load_visit_table()

         
   def load_qtable(self):
         fileToWrite = self.storagePath + self.qTableFile
         import cPickle
         with open(fileToWrite, "rb") as myFile:
             self.qTable = cPickle.load(myFile)
             
             
   def load_visit_table(self):
         fileToWrite = self.storagePath + self.visitFile
         import cPickle
         with open(fileToWrite, "rb") as myFile:
             self.visitTable = cPickle.load(myFile)
