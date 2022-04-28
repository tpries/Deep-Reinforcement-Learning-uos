import cv2
class GridField:

    def __init__(self):
        self.reward = 0
        self.blocked = False
        self.random = False
        self.visited = False
        self.image = cv2.imread(r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images\empty_border.jpg")
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

        final_image = r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images\\"
        final_image += pfad + ".jpg"
        self.image = cv2.imread(final_image)