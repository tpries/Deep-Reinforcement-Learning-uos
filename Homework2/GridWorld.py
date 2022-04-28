import random
from Agent import Agent
from GridField import GridField
from BlockedForm import BlockedForm
import numpy as np

class GridWorld:

    def __init__(self,side_length,multiple_obstacles):

        # only one length bc we only want quadratic envs, must be atleast 5
        assert side_length > 4

        self.agent = Agent()
        self.state_x = 0
        self.state_y = 0

        self.side_length = side_length
        self.field = []

        for row in range(side_length):
            self.field.append([])
            for column in range(side_length):
                self.field[row].append(GridField())

        # set walls
        if multiple_obstacles:
            self._placeWalls(side_length,number_of_walls=side_length-2,size_of_walls=-2)
        else:
            self._placeWalls(side_length,number_of_walls=1,size_of_walls=side_length-1)

        # place positive reward/goal
        # we dont want it to close so a eucl distance of side_length/2 between start and goal at least
        goal_placed = False
        while not goal_placed:
            x = random.randint(0, side_length - 1)
            y = random.randint(0, side_length - 1)

            distance_to_start = x**2 + y**2
            if distance_to_start >= (side_length/2)**2 and not self.field[x][y].isBlocked():
                self.field[x][y].setReward(1)
                goal_placed = True

        # place (side_length*side_length)/5 negative rewards
        for i in range(int((side_length**2)/5)):
            placed = False
            while not placed:
                x = random.randint(0, side_length - 1)
                y = random.randint(0, side_length - 1)

                # conditions
                not_start = not (x == 0 & y == 0)
                not_rewarded = self.field[x][y].getReward() == 0
                not_blocked = not self.field[x][y].isBlocked()

                if not_blocked and not_rewarded and not_start:
                    placed = True
                    self.field[x][y].setReward(round(random.uniform(-1, 0),1))

        # place side_length random fields
        for i in range(3):
            placed = False
            while not placed:
                x = random.randint(0, side_length - 1)
                y = random.randint(0, side_length - 1)

                # conditions
                not_start = not (x == 0 & y == 0)
                not_goal = self.field[x][y].getReward() != 1
                not_blocked = not self.field[x][y].isBlocked()
                not_random = not self.field[x][y].isRandom()

                if not_blocked and not_goal and not_start and not_random:
                    placed = True
                    self.field[x][y].random = True

    def fieldIsBlocked(self,x,y):

        try:
            nb = self.field[x][y]
            is_blocked = nb.isBlocked()
            if is_blocked:
                return True
        except:
            return False

        return False

    def checkNeighbourHood(self,x,y):

        nbh_index_list = [(x-1,y-1),(x,y-1),(x+1,y-1),
                          (x-1,y),(x+1,y),
                          (x-1,y+1),(x,y+1),(x+1,y+1)]

        for nbh_index in nbh_index_list:
            if self.fieldIsBlocked(nbh_index[0],nbh_index[1]):
                return False

        return True

    # maybe export into BlockedForm
    def _placeWalls(self, side_length, number_of_walls=2, size_of_walls=3):

        # we will place side_length -3 obstacles of the size 2
        # they are randomly going to be horizontal or vertical
        #for i in range(int(side_length/3)+1):
        for i in range(2):
            placed_properly = False

            while not placed_properly:
                failed = False

                # list of coordinates that are going to be blocked once we know we can place the wall
                coordinates = []
                wall = BlockedForm(int(side_length/2))

                x = random.randint(0,side_length-1)
                y = random.randint(0,side_length-1)

                # wall cannot block start
                if x == 0 and y == 0:
                    #print(x,y," blocking start")
                    continue

                # wall is already placed here
                this_field = self.field[x][y]
                if this_field.isBlocked():
                    #print(x,y," starting field is blocked")
                    continue

                # no neighouring fields are blocked
                if self.checkNeighbourHood(x,y):
                    coordinates.append((x,y))
                else:
                    #print(x,y," neighbour field is blocked")
                    continue

                while(not wall.isPlaced()):

                    x_direction, y_direction = wall.getDirection()
                    x = x + x_direction
                    y = y + y_direction

                    if x > 4 or x < 0:
                        failed = True
                        break

                    if y > 4 or y < 0:
                        failed = True
                        break

                    # no neighouring fields are blocked
                    if self.checkNeighbourHood(x, y):
                        coordinates.append((x,y))
                    else:
                        #print(x, y, " neighbour field is blocked")
                        failed = True
                        break

                if wall.isPlaced() and not failed:
                    placed_properly = True

                    # it is possible to place the wall
                    # so let's place it
                    for coord in coordinates:
                        #print(coord[0],coord[1])
                        self.field[coord[0]][coord[1]].blocked = True

    def __getitem__(self, position):
        x,y = position

        if x < 0 or x > self.side_length or y < 0 or y > self.side_length:
            return False, False

        field = self.field[x,y]
        return field.isBlocked(), field.getReward()

    def print(self):

        for row in self.field:
            row_string = ""
            for tile in row:

                if tile.isBlocked():
                    row_string += "X"
                else:
                    if tile.getReward() != 0:
                        row_string += str(tile.getReward())
                    elif tile.isRandom():
                        row_string += "?"
                    else:
                        row_string += "0"

                row_string += " "
            print(row_string)

    def step(self,action):
        # check if tile is random
        if self.field[self.state_x][self.state_y].isRandom():
            move = action.getRandomMove()
        else:
            move = action.getMove()

        new_x = int(self.state_x+move[0])
        new_y = int(self.state_y+move[1])
        next_field = self.field[new_x][new_y]

        if next_field.isBlocked():
            #do nothing
            return (self.state_x, self.state_y), 0, False
        else:
            self.field[self.state_x][self.state_y].visited=True

            # update state
            self.state_x = new_x
            self.state_y = new_y
            if next_field.getReward() == 1:
                self.agent += 1
            else:
                self.agent += next_field.getReward()

        return (self.state_x, self.state_y),next_field.getReward(), next_field.isGoal()
