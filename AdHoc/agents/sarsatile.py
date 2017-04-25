# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:11:16 2016

@author: Felipe Leno
"""

from sarsa import SARSA
class SARSATile(SARSA):
    
   useSelfMadeTileCoding = True
   def __init__(self, epsilon=0.1, alpha=0.1, gamma=0.9, decayRate=0.9, seed=12345, port=12345, 
                lowerBoundVariables=-1, upperBoundVariables=+1,serverPath = "../HFO/bin/"):
         super(SARSATile, self).__init__(epsilon=epsilon, alpha=alpha, gamma=gamma, 
            decayRate=decayRate,seed=seed, port=port, serverPath=serverPath)   
            
            
         if self.useSelfMadeTileCoding:
            tilesNumber=10
            tileWidth=0.5
            from tilecoding import TileCoding
            self.cmac = TileCoding(lowerBoundVariables = lowerBoundVariables, 
            upperBoundVariables = upperBoundVariables, tilesNumber = tilesNumber, tileWidth=tileWidth)
         else:
            tilesNumber=10
            tileWidth=4
            from sutton_tilecoding import TileCoding
            self.cmac = TileCoding(tilesNumber = tilesNumber, tileWidth=tileWidth)
            