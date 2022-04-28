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
        pfad= ""
        if self.isBlocked():
            pfad.append("wall_border")
        elif self.isGoal():
            pfad.append("goal")
        elif self.getReward() == 0:
            pfad.append("empty_border")
        elif -1 <= self.getReward() < -0.6:
            pfad.append("lava_border")
        elif -.6 <= self.getReward() < -0.3:
            pfad.append("mittel_border")
        elif -.3 <= self.getReward() < 0:
            pfad.append("klein_border")

        if self.isRandom():
            pfad.append("random_")
        if self.agent_here:
            pfad.append("character")
        elif self.was_visited():
            pfad.append("_trace")

        final_image = r"C:\Users\berit\Deep-Reinforcement-Learning-uos\Homework2\Tile Images\\"
        final_image += pfad + ".jpg"
        self.image = cv2.imread(final_image)