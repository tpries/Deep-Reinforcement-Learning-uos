from GridWorld import GridWorld
import time

def main():

    for i in range(15):
        start_time = time.time()
        random_grid_world = GridWorld(5+i, True)
        random_grid_world.print()
        stop_time = time.time()
        print("Creating a grid world of size: ", i+5, " took: ", stop_time-start_time, " seconds.")
        print("---------------")
if __name__ == "__main__":
    main()