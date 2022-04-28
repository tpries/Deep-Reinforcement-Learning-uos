from GridWorld import GridWorld
from Action import Action
import time
import random

def main():
    for i in range(1):
        random_grid_world = GridWorld(5+i, True)
        random_grid_world.visualize()

        random_grid_world.print()
        for i in range(10):
            action = Action(random.randint(1,4))
            #action.print()
            #print(random_grid_world.step(action))

if __name__ == "__main__":
    main()
