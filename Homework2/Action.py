import random
import numpy as np

class Action:

    def __init__(self,action):
        assert action in [1,2,3,4]
        self.action = action

    def _getDirection(self,action):

        assert action in [1,2,3,4]

        x_move = -99
        y_move = -99

        if action == 1:
            x_move = 0
            y_move = 1

        if action == 2:
            x_move = 0
            y_move = -1

        if action == 2:
            x_move = 1
            y_move = 0

        if action == 2:
            x_move = -1
            y_move = 0

        return [x_move,y_move]


    def getRandomAction(self):
        return self._getDirection(random.randint(1, 4))

    def getMove(self):
        return self._getDirection(self.action)