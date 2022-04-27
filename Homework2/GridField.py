class GridField:

    def __init__(self):
        self.reward = 0
        self.blocked = False
        self.random_factor = 0

    def setReward(self,reward):
        self.reward = reward

    def block(self):
        self.blocked = True

    def setRandomFactor(self,random_factor):
        self.random_factor = random_factor

    def isBlocked(self):
        return self.blocked