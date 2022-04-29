import os
import cv2

class GridField:

    def __init__(self):
        self.reward = 0
        self.blocked = False
        self.random = False
        self.visited = False
        self.agent_here = False

    def setReward(self,reward):
        self.reward = reward

    def getReward(self):
        return self.reward

    def isBlocked(self):
        return self.blocked

    def isRandom(self):
        return self.random

    def isGoal(self):
        return self.reward == 1

    def update(self):
        pfad= ""
        if self.blocked:
            pfad += "wall_border"
        elif self.isGoal():
            pfad += "goal"
        elif self.getReward() == 0:
            pfad += "empty_border"
        elif -1 <= self.getReward() < -0.6:
            pfad += "lava_border"
        elif -.6 <= self.getReward() < -0.3:
            pfad += "mittel_border"
        elif -.3 <= self.getReward() < 0:
            pfad += "klein_border"

        if self.random:
            pfad += "_random"
        if self.agent_here:
            pfad += "_character"
        elif self.visited:
            pfad += "_trace"

        script_dir = os.path.dirname(__file__)
        rel_path = "Tile Images"
        abs_file_path = os.path.join(script_dir, rel_path,pfad+".jpg")
        self.image = cv2.imread(abs_file_path)