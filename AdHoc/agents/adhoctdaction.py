from adhoctd import AdHocTD

class AdHocTDAction(AdHocTD):
        #Enum for importance metrics
    VISIT_IMPORTANCE, Q_IMPORTANCE = range(2)
    
    def __init__(self, budgetAsk=1000, budgetAdvise=1000,stateImportanceMetric=VISIT_IMPORTANCE,seed=12345, port=12345, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, serverPath = "/home/leno/HFO/bin/"):
        super(AdHocTDAction, self).__init__(budgetAsk=budgetAsk,budgetAdvise=budgetAdvise,stateImportanceMetric=stateImportanceMetric,
            port = port, seed=seed, epsilon=epsilon, alpha = alpha, gamma = gamma, decayRate = decayRate,serverPath = serverPath)
        self.informAction = True
 