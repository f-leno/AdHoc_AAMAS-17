# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:05:13 2016
Executes the wilcoxon test to compare the significance of the experiment (open summary file)
@author: Felipe Leno
"""
from scipy.stats import wilcoxon
import csv
import numpy as np


def wilcoxon_test(exp1Dir,exp2Dir,significance=95.0,exp1Name='Alg. 1',exp2Name='Alg. 2'):
    """Opens the summary  files in two given folder and compares the significance of the experiment
    for the two algorithms. The differences greater than a given significance will be printed"""
    print "---Wilcoxon Test---- "+exp1Name+", "+exp2Name + " - Sig. "+str(significance)
    
    desiredP = 1.0 - (significance/100.0)
    #Open the summary files and prepare arrays for comparison
    file1 = open(exp1Dir+"__EVAL_goalpercentages",'r')
    #file1 = open(exp1Dir+"__EVAL_stepscaptured",'r')
    file2 = open(exp2Dir+"__EVAL_goalpercentages",'r')
    #file2 = open(exp2Dir+"__EVAL_stepscaptured",'r')

    reader1 = csv.reader(file1,delimiter=',')
    reader2 = csv.reader(file2,delimiter=',')
    
    #Skipping header
    reader1.next()
    reader2.next()
    
    #Executing the test for all lines
    for line1 in reader1:
        line2 = reader2.next()
        #converting to float
        value1 = np.array(line1[1:], dtype='|S4').astype(np.float)
        value2 = np.array(line2[1:], dtype='|S4').astype(np.float)
        
        #For experiments with different repetition numbers
        if(len(value1)>len(value2)):
           value1 = value1[0:len(value2)]
        elif(len(value2)>len(value1)):     
           value2 = value2[0:len(value1)]
        
        result = wilcoxon(value1,value2)
        if result.pvalue<=desiredP:
            msg = "**Significant Difference: "+line1[0]+","+line2[0]+" "  \
               + "- pValue: "+str(result.pvalue)+ \
               " DiffAvg: "+str(np.average(value1)-np.average(value2))
            print msg
    print "----End of Wilcoxon Test----"
    
if __name__ == '__main__':
    #exp1Dir = "/home/leno/Dropbox/DO - Felipe Leno da Silva/Artigos/NovoArtigo/Data/AdHocTDLoading/"
    exp1Dir = "/home/leno/Dropbox/DO - Felipe Leno da Silva/Artigos/NovoArtigo/Data/Torrey/"
    exp2Dir = "/home/leno/Dropbox/DO - Felipe Leno da Silva/Artigos/NovoArtigo/Data/TorreyAction/"
    #exp2Dir = "/home/leno/Dropbox/DO - Felipe Leno da Silva/Artigos/NovoArtigo/Data/AdHocVisit/" 
    wilcoxon_test(exp1Dir,exp2Dir,95,"EpisodeSharing","SARSA")