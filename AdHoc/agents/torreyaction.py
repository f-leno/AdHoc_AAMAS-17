# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:00:08 2016

@author: Felipe Leno
Torrey & Taylor importance correcting Advising implementation
"""

from torrey import Torrey



class TorreyAction(Torrey):
    
   def __init__(self, budget=1000,threshold = 0.01,seed=12345, port=12345, serverPath = "/home/leno/HFO/bin/"):
        super(TorreyAction, self).__init__(budget=budget,threshold=threshold,seed=seed,port=port,serverPath=serverPath)
        self.informAction = True
       
        
  