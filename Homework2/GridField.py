class GridField:

    def __init__(self):
        self.reward = 0
        self.blocked = False
        self.random_factor = 0

    def setReward(self,reward):
        self.reward = reward

    def getReward(self):
        return self.reward

    def block(self):
        self.blocked = True

    def randomize(self):
        self.random_factor = 0.25

    def isBlocked(self):
        return self.blocked

    def isRandom(self):
        return self.random_factor != 0