
class Agent:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self,x,y):
        self.x += x
        self.y += y