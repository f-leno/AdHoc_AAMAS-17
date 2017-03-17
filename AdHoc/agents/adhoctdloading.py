# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 08:36:39 2016
AdHocTD advising with an already trained agent
@author: Felipe Leno
"""

from adhoctd import AdHocTD
class AdHocTDLoading(AdHocTD):

   storagePath = None
   visitTable = None
   qTableFile = 'QTable.txt'
   visitFile = 'VisitTable.txt'
    
    
   def __init__(self, budgetAsk=0, budgetAdvise=1000,seed=12345, port=12345, 
                 epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/",storagePath="agentData/"):
        super(AdHocTDLoading, self).__init__(budgetAsk=budgetAsk,budgetAdvise=budgetAdvise,
                port = port, seed=seed,serverPath = serverPath)
        self.informAction = False
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
             
   #Erase Here          
  # def check_advise(self,stateFeatures,state): 
  #      advisedAction = self.select_action(stateFeatures,state,True)
  #      return True,advisedAction 