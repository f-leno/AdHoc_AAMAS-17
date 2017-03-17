# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:36:47 2016

@author: Felipe Leno
Loads everything from adhoc.py, this class only defines parameters for the visit-based
ad hoc advising
"""
from adhoc import AdHoc
import math
class AdHocVisit(AdHoc):
        #Enum for importance metrics
    VISIT_IMPORTANCE, Q_IMPORTANCE = range(2)
    
    def __init__(self, budgetAsk=1000, budgetAdvise=1000,stateImportanceMetric=VISIT_IMPORTANCE,seed=12345, port=12345, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/"):
        super(AdHocVisit, self).__init__(budgetAsk,budgetAdvise,stateImportanceMetric,port = port, seed=seed,serverPath = serverPath)
        
        
    def midpoint(self,typeMid):
        """Calculates the midpoint"""     
        if typeMid == self.ADVISE:
           numVisits = 25
           impMid = numVisits / (numVisits + math.log(self.scalingVisits + numVisits))
           return impMid
        elif typeMid == self.ASK:
            numVisits = 20
            impMid = numVisits / (numVisits + math.log(self.scalingVisits + numVisits))
            return impMid
            
        #Error
        return None