# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:13:25 2016

@author: Felipe Leno
Tile Coding simple implementation - based on the description given by http://web.cs.ucla.edu/~sherstov/pdf/sara05-tiling.pdf
"""

import math
class TileCoding():
    upperBoundVariable = None    
    lowerBoundVariable = None
    t = None
    w = None
    tileList = []
    def __str__(self):
        return "TileCoding. Params: UpperBoundVariable: "+str(self.upperBoundVariable)+ \
        ", LowerBoundVariable: "+str(self.lowerBoundVariable)+", NumberOfTiles: "+str(self.t)+ \
        ", TilesWidth: "+str(self.w)
        
    def quantize(self,features):
        """Quantize the features, returns a list containing the value of the tiles for each variable
          The return is a array of arrays, each array consists in the value of a tile for all variables"""
        resultList = []
          
        #Computes the value of each tile    
        for tile in range(0,len(self.tileList)):
          lowLimit = self.tileList[tile][0]
          upperLimit = self.tileList[tile][1]
          
          #Calculates the tile value for all features
          activated = []
          for feature in features:
              test = feature <= upperLimit and feature >= lowLimit
              value = 1 if test==True else 0
              activated.append(value)
          #Include the results for this tile in the return list
          resultList.append(activated)
          
          #Inserted for compactibility
          data = []
          #len(quantVar[0]) is the number of variables
          for i in range(0,len(resultList[0])):
            #Transforms n tuples into a single array
            for var in resultList:
                #copy each tuple value to the output
                data.append(var[i])

        return data
              
    
    
    
    def __init__(self, lowerBoundVariables, upperBoundVariables, tilesNumber,tileWidth):
         self.upperBoundVariable = float(upperBoundVariables)
         self.lowerBoundVariable = float(lowerBoundVariables)
         self.t = tilesNumber
         self.w = float(tileWidth)
         
         self.stepTile = (self.upperBoundVariable - self.lowerBoundVariable) / (tilesNumber)
         
         if(math.fabs(tileWidth) < math.fabs(self.stepTile)):
             print "****Warning - The tileWidth is too low, this tile coding parameterization is prone to be misleading***"
         lastStep = lowerBoundVariables
         #Compute the tiles
         for i in range(0,self.t):
             currentTile = [lastStep,lastStep+self.w]
             self.tileList.append(currentTile)
             lastStep = lastStep+self.stepTile
























#import math
#import Tiles.tiles as tiles
#class TileCoding():
#    upperBoundVariable = None    
#    lowerBoundVariable = None
#    t = None
#    w = None
#    col = None
#    tileList = []
#    def __str__(self):
#        return "TileCoding. Params: UpperBoundVariable: "+str(self.upperBoundVariable)+ \
#        ", LowerBoundVariable: "+str(self.lowerBoundVariable)+", NumberOfTiles: "+str(self.t)+ \
#        ", TilesWidth: "+str(self.w)
#        
#    def quantize(self,features):
#        """Quantize the features, returns a list containing the value of the tiles for each variable
#          The return is a array of arrays, each array consists in the value of a tile for all variables"""
# 
#        resultList = []
#        
#        #Computes the value of tiles for each feature    
#        #for feature in features:
#        #    resultList.extend(tiles.tiles(self.t,self.col,[feature]))
#        resultList.extend(tiles.tiles(self.t,self.col,features))
#        
# 
#        return resultList  
#    
#    
#    
#    def __init__(self, tilesNumber,tileWidth):
#            self.t = tilesNumber
#            self.w = int(tileWidth)
#            self.col = tiles.CollisionTable(self.w,'unsafe')
#        
#            
#           
#    
#
#    def legacy_quantize(self):
#
#        #lowerBoundVariables, upperBoundVariables, tilesNumber,tileWidth
#
#         self.upperBoundVariable = float(upperBoundVariables)
#         self.lowerBoundVariable = float(lowerBoundVariables)
#         self.t = tilesNumber
#         self.w = float(tileWidth)
#         
#         self.stepTile = (self.upperBoundVariable - self.lowerBoundVariable) / (tilesNumber)
#         
#         if(math.fabs(tileWidth) < math.fabs(self.stepTile)):
#             print "****Warning - The tileWidth is too low, this tile coding parameterization is prone to be misleading***"
#         lastStep = lowerBoundVariables
#         #Compute the tiles
#         for i in range(0,self.t):
#             currentTile = [lastStep,lastStep+self.w]
#             self.tileList.append(currentTile)
#             lastStep = lastStep+self.stepTile
#
#
#
#         resultList = []
#          
#         #Computes the value of each tile    
#         for tile in range(0,len(self.tileList)):
#           lowLimit = self.tileList[tile][0]
#           upperLimit = self.tileList[tile][1]
#          
#           #Calculates the tile value for all features
#           activated = []
#           for feature in features:
#              test = feature <= upperLimit and feature >= lowLimit
#              value = 1 if test==True else 0
#              activated.append(value)
#          #Include the results for this tile in the return list
#           resultList.append(activated)
#
#         return resultList
#        
#        
#        
#if __name__ == '__main__':
#    print TileCoding(5,4).quantize([1.0,1.0,0.5,-0.5])       
#        
#        