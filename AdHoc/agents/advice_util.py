# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:18:57 2016

@author: Felipe Leno
This file implements methods to make the communication between advisees and advisors
This agent communicates through references.
TODO: an actual message passing implementation through different processes
"""


class AdviceUtil():
    
    advisors = None
    
    def setupAdvisors(self,advisors):
        self.advisors = advisors

    def ask_advice(self,uNum,state,action=None):
         """This method is executed when the advisee asks for advice.
           A file is created in the askFolder with the uNum, the agent waits for a while
           in order to wait for advice, then reads the response file in adviceFolder and erases
           all files, returning the advised action
           uNum - the Uniform number of the advisee
           state - the advisee state after it is processed in the statespace_util methods
           action - the action the agent is willing to take, in case of action informant agents
           """
         advice = []
         
         for advisor in self.advisors:
             a = advisor.advise_action(uNum,state,action)
             
             #Check if any advice was received
             if a:
                 advice.append(a)
         return advice

