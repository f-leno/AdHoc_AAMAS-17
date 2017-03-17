# -*- coding: utf-8 -*-
"""


@author: Felipe Leno
Tile Coding Sutton implementation
"""
import math
import Tiles.tiles as tiles
class TileCoding():
    upperBoundVariable = None    
    lowerBoundVariable = None
    t = None
    w = None
    col = None
    tileList = []
    def __str__(self):
        return "TileCoding. Params: UpperBoundVariable: "+str(self.upperBoundVariable)+ \
        ", LowerBoundVariable: "+str(self.lowerBoundVariable)+", NumberOfTiles: "+str(self.t)+ \
        ", TilesWidth: "+str(self.w)
        
    def quantize(self,features):
        """Quantize the features, returns a list containing the value of the tiles for each variable
          The return is a array of arrays, each array consists in the value of a tile for all variables"""
 
        resultList = []
        
        #Computes the value of tiles for each feature    
        #for feature in features:
        #    resultList.extend(tiles.tiles(self.t,self.col,[feature]))
        resultList.extend(tiles.tiles(self.t,self.col,features))
        
 
        return resultList  
    
    
    
    def __init__(self, tilesNumber,tileWidth):
            self.t = tilesNumber
            self.w = int(tileWidth)
            self.col = tiles.CollisionTable(self.w,'unsafe')
        
            
        
        
if __name__ == '__main__':
    print TileCoding(5,4).quantize([1.0,1.0,0.5,-0.5])       
        
        