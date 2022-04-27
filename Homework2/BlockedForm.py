import random

class BlockedForm:

    def __init__(self,size):
        # throwing a coin
        # is wall going to be horizontal or vertical
        if bool(random.getrandbits(1)):
            self.width = size
            self.height = 1
        else:
            self.width = 1
            self.height = size

        self.wall_index = 0

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    # walk along wall and give direction of next pice of wall
    # returns true when complete wall is walked of
    def getDirection(self):

        if self.isPlaced():
            return 0,0

        if self.width > self.height:
            self.wall_index += 1
            return 1,0
        else:
            self.wall_index += 1
            return 0,1

    def isPlaced(self):
        if self.wall_index+1 == max(self.width,self.height):
            return True
        else:
            return False