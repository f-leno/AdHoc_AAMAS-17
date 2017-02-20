from hfo import *
import random

import abc

class Agent(object):
    """ This is the base class for all agent implementations.

    """
    __metaclass__ = abc.ABCMeta
    
    connectPath = ""
    connectPort = 0

    ''' The HFO object '''
    #hfo = None
    ''' State discretizations '''
    #cmac = None

    ''' An enum of the possible HFO actions
      [Low-Level] Dash(power, relative_direction)
      [Low-Level] Turn(direction)
      [Low-Level] Tackle(direction)
      [Low-Level] Kick(power, direction)
      [Mid-Level] Kick_To(target_x, target_y, speed)
      [Mid-Level] Move(target_x, target_y)
      [Mid-Level] Dribble(target_x, target_y)
      [Mid-Level] Intercept(): Intercept the ball
      [High-Level] Move(): Reposition player according to strategy
      [High-Level] Shoot(): Shoot the ball
      [High-Level] Pass(teammate_unum): Pass to teammate
      [High-Level] Dribble(): Offensive dribble
      [High-Level] Catch(): Catch the ball (Goalie Only)
      NOOP(): Do Nothing
      QUIT(): Quit the game '''
    DASH, TURN, TACKLE, KICK, KICK_TO, MOVE_TO, DRIBBLE_TO, INTERCEPT, \
      MOVE, SHOOT, PASS, DRIBBLE, CATCH, NOOP, QUIT = range(15)

    #Customized actions
    PASSnear = 15
    PASSfar = 16
    #The available actions
    actions = [MOVE, SHOOT, PASSnear, PASSfar, DRIBBLE]

    ''' Possible game status
      [IN_GAME] Game is currently active
      [GOAL] A goal has been scored by the offense
      [CAPTURED_BY_DEFENSE] The defense has captured the ball
      [OUT_OF_BOUNDS] Ball has gone out of bounds
      [OUT_OF_TIME] Trial has ended due to time limit
      [SERVER_DOWN] Server is not alive '''
    IN_GAME, GOAL, CAPTURED_BY_DEFENSE, OUT_OF_BOUNDS, OUT_OF_TIME, \
      SERVER_DOWN = range(6)

    ''' Possible sides '''
    RIGHT, NEUTRAL, LEFT = range(-1,2)


    '''State Variable Enum (with 2 friendly agents and 1 opponent)'''
    X_POSITION, Y_POSITION, ORIENTATION, BALL_PROXIMITY, BALL_ANGLE, \
      ABLE_KICK, CENTER_PROXIMITY, GOAL_ANGLE, GOAL_OPENING, \
      OPPONENT_PROXIMITY, FRIEND1_GOAL_OPPENING, FRIEND2_GOAL_OPPENING, \
      FRIEND1_OPP_PROXIMITY, FRIEND2_OPP_PROXIMITY, FRIEND1_OPENING, \
      FRIEND2_OPENING, FRIEND1_PROXIMITY, FRIEND1_ANGLE, FRIEND1_NUMBER, \
      FRIEND2_PROXIMITY, FRIEND2_ANGLE, FRIEND2_NUMBER, OPP_PROXIMITY, \
      OPP_ANGLE, OPP_NUMBER = range(25)

    #def __init__(self, friends=3, opps=1):
    def __init__(self, seed=12345, port=12345, serverPath = "/home/leno/HFO/bin/"):
        """ Initializes an agent for a given environment. """
        '''
        if friends == 0:
            self.actions = [self.MOVE, self.SHOOT, self.DRIBBLE]
        elif friends == 1:
            self.actions = [self.MOVE, self.SHOOT, self.DRIBBLE, self.PASS]
        else:
            self.actions = [self.MOVE, self.SHOOT, self.DRIBBLE, \
                            self.PASSnear, self.PASSfar]
        # every agent has those state features
        # friendly players goal opening angle
        for friend in range(friends):
            self.
        # friendly players proximity to opponent

        # friendly players pass opening angle1.

        # friendly players proxmity, angle & unum

        # opposing players proximity. angle & unum
        '''
        self.hfo = HFOEnvironment()
        self.connectPath = serverPath+'teams/base/config/formations-dt'
        self.connectPort = port
        self.exploring = True
        self.training_steps_total = 0
        # set the agent seed
        random.seed(seed)

    def connectHFO(self):
        """Connects in the server"""
        print('***** Connecting to HFO server on port %s' % str(self.connectPort))
        serverResponse = self.hfo.connectToServer(
                feature_set=HIGH_LEVEL_FEATURE_SET,
                config_dir=self.connectPath,
                server_port=self.connectPort,
                server_addr='localhost',
                team_name='base_left',
                play_goalie=False)
        print('***** Problems while connecting? %s'% str(serverResponse))
        self.unum = self.hfo.getUnum()
        
    @abc.abstractmethod  
    def advise_action(self,uNum,state):
        """Verifies if the agent can advice a friend, and return the action if possible"""
        pass
    @abc.abstractmethod
    def setupAdvising(self,agentIndex,allAgents):
        """ This method is called in preparation for advising """
        pass
    @abc.abstractmethod
    def select_action(self, stateFeatures, state, noAdvice=False):
        """ When this method is called, the agent executes an action. """
        pass

    @abc.abstractmethod
    def observe_reward(self,state,action,reward,statePrime):
        """ After executing an action, the agent is informed about the state-action-reward-state tuple """
        pass

    @abc.abstractmethod
    def step(self, state, action):
        """ Perform a complete training step """
        pass

    def set_exploring(self, exploring):
        """ The agent keeps track if it should explore in the current state (used for evaluations) """
        self.exploring = exploring


    def get_reward(self, status):
        """The Reward Function returns -1 when a defensive agent captures the ball,
        +1 when the agent's team scores a goal and 0 otherwise"""
        if(status == self.CAPTURED_BY_DEFENSE):
             return -1.0
        elif(status == self.OUT_OF_BOUNDS):
             return -1.0
        elif(status == self.OUT_OF_TIME):
             return 0
        elif(status == self.GOAL):
             return 1.0
        return 0

    def execute_action(self, action):
        """Executes the action in the HFO server"""
        #If the action is not one of the default ones, it needs translation
        if action in range(15):
            self.hfo.act(action)
        else:
            #In the statespace_util file
            action, parameter = self.translate_action(action, self.hfo.getState())
            self.hfo.act(action, parameter)

    def translate_action(self, action, stateFeatures):
        """Defines the nearest and farthest friendly agents,
        then return the PASS action with the correct parameter"""
        nearest = 0
        farthest = 0

        if(stateFeatures[self.FRIEND1_PROXIMITY] > stateFeatures[self.FRIEND2_PROXIMITY]):
            nearest = stateFeatures[self.FRIEND1_NUMBER]
            farthest = stateFeatures[self.FRIEND2_NUMBER]
        else:
            nearest = stateFeatures[self.FRIEND2_NUMBER]
            farthest = stateFeatures[self.FRIEND1_NUMBER]
        actionRet = self.PASS

        if(action == self.PASSnear):
            argument = nearest
        elif(action == self.PASSfar):
            argument = farthest
        else:
            print "ERROR ACTION: "+str(action)

        return actionRet, argument


    def get_transformed_features(self, stateFeatures):
        """Erases the irrelevant features (such as agent Unums) and sort agents by
        their distance"""
        #Defines the agent order
        if(stateFeatures[self.FRIEND1_PROXIMITY] > stateFeatures[self.FRIEND2_PROXIMITY]):
            nearestGoalOpening = stateFeatures[self.FRIEND1_GOAL_OPPENING]
            nearestOppProximity = stateFeatures[self.FRIEND1_OPP_PROXIMITY]
            nearestOpening = stateFeatures[self.FRIEND1_OPENING]
            nearestProximity = stateFeatures[self.FRIEND1_PROXIMITY]
            nearestAngle = stateFeatures[self.FRIEND1_ANGLE]

            farthestGoalOpening = stateFeatures[self.FRIEND2_GOAL_OPPENING]
            farthestOppProximity = stateFeatures[self.FRIEND2_OPP_PROXIMITY]
            farthestOpening = stateFeatures[self.FRIEND2_OPENING]
            farthestProximity = stateFeatures[self.FRIEND2_PROXIMITY]
            farthestAngle = stateFeatures[self.FRIEND2_ANGLE]
        else:
            nearestGoalOpening = stateFeatures[self.FRIEND2_GOAL_OPPENING]
            nearestOppProximity = stateFeatures[self.FRIEND2_OPP_PROXIMITY]
            nearestOpening = stateFeatures[self.FRIEND2_OPENING]
            nearestProximity = stateFeatures[self.FRIEND2_PROXIMITY]
            nearestAngle = stateFeatures[self.FRIEND2_ANGLE]

            farthestGoalOpening = stateFeatures[self.FRIEND1_GOAL_OPPENING]
            farthestOppProximity = stateFeatures[self.FRIEND1_OPP_PROXIMITY]
            farthestOpening = stateFeatures[self.FRIEND1_OPENING]
            farthestProximity = stateFeatures[self.FRIEND1_PROXIMITY]
            farthestAngle = stateFeatures[self.FRIEND1_ANGLE]

        stateFeatures[self.FRIEND1_GOAL_OPPENING] = nearestGoalOpening
        stateFeatures[self.FRIEND1_OPP_PROXIMITY] = nearestOppProximity
        stateFeatures[self.FRIEND1_OPENING] = nearestOpening
        stateFeatures[self.FRIEND1_PROXIMITY] = nearestProximity
        stateFeatures[self.FRIEND1_ANGLE] = nearestAngle

        stateFeatures[self.FRIEND2_GOAL_OPPENING] = farthestGoalOpening
        stateFeatures[self.FRIEND2_OPP_PROXIMITY] = farthestOppProximity
        stateFeatures[self.FRIEND2_OPENING] = farthestOpening
        stateFeatures[self.FRIEND2_PROXIMITY] = farthestProximity
        stateFeatures[self.FRIEND2_ANGLE] = farthestAngle


        # Remaining features:
        # CENTER_PROXIMITY, GOAL_ANGLE, GOAL_OPENING, OPPONENT_PROXIMITY,
        # FRIEND1_GOAL_OPPENING. FRIEND2_GOAL_OPPENING
        #stateFeatures = np.delete(stateFeatures,[self.FRIEND1_NUMBER,self.FRIEND2_NUMBER])
        stateFeatures = np.delete(stateFeatures,
                                    [self.X_POSITION,
                                     self.Y_POSITION,
                                     self.ORIENTATION,
                                     self.BALL_PROXIMITY,
                                     self.BALL_ANGLE,
                                     #self.ABLE_KICK,
                                     self.FRIEND1_OPP_PROXIMITY,
                                     self.FRIEND2_OPP_PROXIMITY,
                                     self.FRIEND1_OPENING,
                                     self.FRIEND2_OPENING,
                                     self.FRIEND1_PROXIMITY,
                                     self.FRIEND1_ANGLE,
                                     self.FRIEND1_NUMBER,
                                     self.FRIEND2_PROXIMITY,
                                     self.FRIEND2_ANGLE,
                                     self.FRIEND2_NUMBER,
                                     self.OPP_PROXIMITY,
                                     self.OPP_ANGLE,
                                     self.OPP_NUMBER#])
                                     ,self.OPPONENT_PROXIMITY])


        return tuple(stateFeatures.tolist())

    '''
    def get_transformed_features(self, stateFeatures):
        """Erases the irrelevant features (such as agent Unums) and sort agents by
        their distance"""
        transformedFeatures = []
        transformedFeatures[self.CENTER_PROXIMITY] = stateFeatures[self.CENTER_PROXIMITY]
        transformedFeatures[self.GOAL_ANGLE] = stateFeatures[self.GOAL_ANGLE]
        transformedFeatures[self.GOAL_OPENING] = stateFeatures[self.GOAL_OPENING]
        transformedFeatures[self.OPPONENT_PROXIMITY] = stateFeatures[self.OPPONENT_PROXIMITY]
        if(stateFeatures[self.FRIEND1_PROXIMITY] > stateFeatures[self.FRIEND2_PROXIMITY]):
            transformedFeatures[self.FRIEND1_GOAL_OPPENING] = stateFeatures[self.FRIEND1_GOAL_OPPENING]
            transformedFeatures[self.FRIEND2_GOAL_OPPENING] = stateFeatures[self.FRIEND2_GOAL_OPPENING]
        else:
            transformedFeatures[self.FRIEND1_GOAL_OPPENING] = stateFeatures[self.FRIEND2_GOAL_OPPENING]
            transformedFeatures[self.FRIEND2_GOAL_OPPENING] = stateFeatures[self.FRIEND1_GOAL_OPPENING]
        return tuple(transformedFeatures.tolist())
    '''

    def get_Unum(self):
        return self.hfo.getUnum()
    
    def finish_training(self):
        """End the training"""
        pass

    def get_used_budget(self):
        """Returns the ask budget the agent already used"""
        return 0
