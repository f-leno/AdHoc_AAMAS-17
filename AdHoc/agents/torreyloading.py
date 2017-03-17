# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 08:11:42 2016
Implementation of Torrey Loading a qTable
@author: Felipe Leno
"""

from torrey import Torrey


class TorreyLoading(Torrey):
   storagePath = None
   qTableFile = 'QTable.txt'
    
   
   def __init__(self, budget=1000,threshold = 0.01,seed=12345, port=12345, serverPath = "/home/leno/HFO/bin/",
                storagePath="agentData/"):
         super(TorreyLoading, self).__init__(budget=budget, threshold=threshold,seed=seed, port=port, serverPath=serverPath)          
         self.storagePath = storagePath
         self.load_qtable()
         
   def load_qtable(self):
         fileToWrite = self.storagePath + self.qTableFile
         import cPickle
         with open(fileToWrite, "rb") as myFile:
             self.qTable = cPickle.load(myFile)