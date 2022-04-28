from GridWorld import GridWorld
from Action import Action
import time
import random

def main():
    for i in range(1):
        random_grid_world = GridWorld(10+i, False)
        random_grid_world.visualize()


        for i in range(50):
            action = Action(random.randint(1,4))
            random_grid_world.step(action)
            random_grid_world.visualize()

if __name__ == "__main__":
    main()
