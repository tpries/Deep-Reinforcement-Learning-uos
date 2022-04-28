import cv2
class GridField:

    def __init__(self):
        self.reward = 0
        self.blocked = False
        self.random = False
        self.was_visited = False
        self.image = cv2.imread(r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images\empty_border.jpg")

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

    @property
    def visited(self):
        return self.was_visited

    def update(self):
