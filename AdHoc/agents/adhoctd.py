"""
@author: Felipe Leno

Specialized implementation of ad hoc advising using confidence function based on both
number of visits and differences in Q-values.
"""

from adhoc import AdHoc
import math
import random
class AdHocTD(AdHoc):
        #Enum for importance metrics
    VISIT_IMPORTANCE, Q_IMPORTANCE = range(2)
    
    def __init__(self, budgetAsk=1000, budgetAdvise=1000,stateImportanceMetric=VISIT_IMPORTANCE,seed=12345, port=12345, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/"):
        super(AdHocTD, self).__init__(budgetAsk,budgetAdvise,stateImportanceMetric,port = port, seed=seed,serverPath = serverPath)
        self.informAction = False
        print "Param: "+str(0.9)+" - "+str(0.5)
        
        
    def midpoint(self,typeMid):
        """Calculates the midpoint"""     
        if typeMid == self.ASK:
            numVisits = 10
            impMid = numVisits / (numVisits + math.log(self.scalingVisits + numVisits))
            return impMid
            
        #Error
        return None
        
    def check_advise(self,stateFeatures,state): 
        """Returns if the agent should advice in this state.
        The advised action is also returned in the positive case"""
            
        processedState = self.quantize_features(state)
        numberVisits = self.number_visits(processedState)
         
        
        if numberVisits == 0:
            return False,None
        
        
        maxQ = -float("inf")
        minQ = float("inf")
        #Get max and min Q value
        actions = [self.DRIBBLE, self.SHOOT, self.PASSfar, self.PASSnear]
        for act in actions:
            if (processedState,act) in self.qTable:
                actQ = self.qTable.get((processedState, act),0)
                if actQ > maxQ:
                    maxQ = actQ
                if actQ < minQ:
                    minQ = actQ
            
            # print "MaxQ "+str(maxQ)
            # print "MinQ "+str(minQ)
            # print "len "+str(len(actions))
        difQ = math.fabs(maxQ - minQ)

        #param = 1.5
        param = 1.5
        
        
        value = (math.sqrt(numberVisits) * difQ )
        
        #Calculates the probability
        prob = 1 - (math.pow((1 + param),-value))
        
      
        ##
        #processedState = self.quantize_features(state)
        #numberVisits = self.number_visits(processedState)
        #if importance>0:        
            #print str(importance)+"  -  "+str(prob)
        ##
        #Check if the agent should advise
        if random.random() < prob: #and prob > 0.1:
            advisedAction = self.select_action(stateFeatures,state,True)
            return True,advisedAction          
            
        return False,None
        
    def check_ask(self,state):
        """Returns if the agent should ask for advise in this state"""
        
        if self.exploring and not (self.quantize_features(state) in self.advisedState):
            processedState = self.quantize_features(state)
            numberVisits = self.number_visits(processedState)
            if numberVisits == 0:
                return True
            
            #param = 0.5
            param = 0.5
            #Calculates the probability
            prob =  math.pow((1 + param),-math.sqrt(numberVisits))
            
            ##
            #processedState = self.quantize_features(state)
            #numberVisits = self.number_visits(processedState)
            #print str(numberVisits)+"  -  "+str(prob)
            ##
            
            if random.random() < prob: #and prob > 0.1:
                return True
        return False