# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:54:23 2016

@author: Felipe Leno

This file implements Utilities for state space processing
"""

from agents.agent import Agent #importing the action enum
import numpy as np

"""State Variable Enum (with 2 friendly agents and 1 opponent)"""
X_POSITION, Y_POSITION, ORIENTATION, BALL_PROXIMITY, BALL_ANGLE, ABLE_KICK, CENTER_PROXIMITY, GOAL_ANGLE, \
      GOAL_OPENING, OPPONENT_PROXIMITY, FRIEND1_GOAL_OPPENING, FRIEND2_GOAL_OPPENING, \
      FRIEND1_OPP_PROXIMITY, FRIEND2_OPP_PROXIMITY, FRIEND1_OPENING, FRIEND2_OPENING, \
      FRIEND1_PROXIMITY, FRIEND1_ANGLE, FRIEND1_NUMBER, FRIEND2_PROXIMITY, FRIEND2_ANGLE, FRIEND2_NUMBER, \
      OPP_PROXIMITY, OPP_ANGLE, OPP_NUMBER = range(25)



def translate_action(action, stateFeatures):
    """Defines the nearest and farthest friendly agents,
    then return the PASS action with the correct parameter"""
    nearest = 0
    farthest = 0

    if(stateFeatures[FRIEND1_PROXIMITY] > stateFeatures[FRIEND2_PROXIMITY]):
        nearest = stateFeatures[FRIEND1_NUMBER]
        farthest = stateFeatures[FRIEND2_NUMBER]
    else:
        nearest = stateFeatures[FRIEND2_NUMBER]
        farthest = stateFeatures[FRIEND1_NUMBER]
    actionRet = Agent.PASS

    if(action==Agent.PASSnear):
        argument = nearest
    elif(action==Agent.PASSfar):
        argument = farthest

    return actionRet,argument


def get_transformed_features(stateFeatures):
    """Erases the irrelevant features (such as agent Unums) and sort agents by
    their distance"""
    #Defines the agent order
    if(stateFeatures[FRIEND1_PROXIMITY] > stateFeatures[FRIEND2_PROXIMITY]):
        nearestGoalOpening = stateFeatures[FRIEND1_GOAL_OPPENING]
        nearestOppProximity = stateFeatures[FRIEND1_OPP_PROXIMITY]
        nearestOpening = stateFeatures[FRIEND1_OPENING]
        nearestProximity = stateFeatures[FRIEND1_PROXIMITY]
        nearestAngle = stateFeatures[FRIEND1_ANGLE]

        farthestGoalOpening = stateFeatures[FRIEND2_GOAL_OPPENING]
        farthestOppProximity = stateFeatures[FRIEND2_OPP_PROXIMITY]
        farthestOpening = stateFeatures[FRIEND2_OPENING]
        farthestProximity = stateFeatures[FRIEND2_PROXIMITY]
        farthestAngle = stateFeatures[FRIEND2_ANGLE]
    else:
        nearestGoalOpening = stateFeatures[FRIEND2_GOAL_OPPENING]
        nearestOppProximity = stateFeatures[FRIEND2_OPP_PROXIMITY]
        nearestOpening = stateFeatures[FRIEND2_OPENING]
        nearestProximity = stateFeatures[FRIEND2_PROXIMITY]
        nearestAngle = stateFeatures[FRIEND2_ANGLE]

        farthestGoalOpening = stateFeatures[FRIEND1_GOAL_OPPENING]
        farthestOppProximity = stateFeatures[FRIEND1_OPP_PROXIMITY]
        farthestOpening = stateFeatures[FRIEND1_OPENING]
        farthestProximity = stateFeatures[FRIEND1_PROXIMITY]
        farthestAngle = stateFeatures[FRIEND1_ANGLE]

    stateFeatures[FRIEND1_GOAL_OPPENING] = nearestGoalOpening
    stateFeatures[FRIEND1_OPP_PROXIMITY] = nearestOppProximity
    stateFeatures[FRIEND1_OPENING] = nearestOpening
    stateFeatures[FRIEND1_PROXIMITY] = nearestProximity
    stateFeatures[FRIEND1_ANGLE] = nearestAngle

    stateFeatures[FRIEND2_GOAL_OPPENING] = farthestGoalOpening
    stateFeatures[FRIEND2_OPP_PROXIMITY] = farthestOppProximity
    stateFeatures[FRIEND2_OPENING] = farthestOpening
    stateFeatures[FRIEND2_PROXIMITY] = farthestProximity
    stateFeatures[FRIEND2_ANGLE] = farthestAngle

    #Removes the agent Unum... makes the friendly agents differentiable only by their feature values
    # and makes easier the state translation for the advising
    stateFeatures = np.delete(stateFeatures,[FRIEND1_NUMBER,FRIEND2_NUMBER])
    return stateFeatures
