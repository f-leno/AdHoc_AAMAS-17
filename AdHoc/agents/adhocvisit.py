from adhoc import AdHoc
import math
import random
class AdHocVisit(AdHoc):
        #Enum for importance metrics
    VISIT_IMPORTANCE, Q_IMPORTANCE = range(2)
    
    def __init__(self, budgetAsk=1000, budgetAdvise=1000,stateImportanceMetric=VISIT_IMPORTANCE,seed=12345, port=12345, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/"):
        super(AdHocVisit, self).__init__(budgetAsk,budgetAdvise,stateImportanceMetric,port = port, seed=seed,serverPath = serverPath)
        self.informAction = False
        
        
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
        
        #param = 0.2  #-> Experiments Action and NoAction
        param = 0.4
        #param = 1.5
        #Calculates the probability
        prob = 1 - math.pow((1 + param),-math.log(numberVisits,2))#math.log(numberVisits,2))#
        ##
        #processedState = self.quantize_features(state)
        #numberVisits = self.number_visits(processedState)
        #if importance>0:        
            #print str(importance)+"  -  "+str(prob)
        ##
        #Check if the agent should advise
        if random.random() < prob: #and prob > 0.1:
            advisedAction = self.select_action(stateFeatures,state,True)
            #print "Advised: prob:"+str(prob)+" visits: "+str(numberVisits)
            return True,advisedAction          
            
        return False,None
        
    def check_ask(self,state):
        """Returns if the agent should ask for advise in this state"""
        
        if self.exploring and not (self.quantize_features(state) in self.advisedState):
            processedState = self.quantize_features(state)
            numberVisits = self.number_visits(processedState)
            if numberVisits == 0:
                return True
            
            param = 0.5
            #Calculates the probability
            prob =  math.pow((1 + param),-math.sqrt(numberVisits))
            
            ##
            #processedState = self.quantize_features(state)
            #numberVisits = self.number_visits(processedState)
            #print str(numberVisits)+"  -  "+str(prob)
            ##
            
            if random.random() < prob: #and prob > 0.1:
                #print "Asked: prob:"+str(prob)+" visits: "+str(numberVisits)
                return True
        return False