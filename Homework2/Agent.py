import numpy as np

class Agent:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.reward = 0

    def move(self,x,y):
        self.x += x
        self.y += y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __add__(self,reward):
        self.reward += reward