import random

from GridField import GridField
from BlockedForm import BlockedForm

class GridWorld:

    def __init__(self,side_length,multiple_obstacles):

        # only one length bc we only want quadratic envs, must be atleast 5
        assert side_length > 4

        self.side_length = side_length
        self.field = []

        for row in range(side_length):
            self.field.append([])
            for column in range(side_length):
                self.field[row].append(GridField())

        self._placeMultipleWalls(side_length)

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

    def _placeMultipleWalls(self,side_length):

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
                        self.field[coord[0]][coord[1]].block()

    def _placeOneWall(self,side_length):
        pass

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
                    row_string += "X-"
                else:
                    row_string += "O-"
            print(row_string)