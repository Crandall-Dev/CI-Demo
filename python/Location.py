##
#   General Location (coordinate) class
#
#   @author Aaron S. Crandall <crandall@gonzaga.edu>
#   @copyright 2020
#


from Direction import Direction
from Exceptions import SameLocations


# *************************************************************************** #
class Location(object):
    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def to_JSON(self):
        return "{\"x\": " + str(self.x) + ", \"y\": " + str(self.y) + "}"

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __add__(self, dir):
        if dir == Direction.NORTH:
            return Location(x=self.x, y=self.y - 1)
        elif dir == Direction.SOUTH:
            return Location(x=self.x, y=self.y + 1)
        elif dir == Direction.EAST:
            return Location(x=self.x + 1, y=self.y)
        elif dir == Direction.WEST:
            return Location(x=self.x - 1, y=self.y)

    def calc_direction_to(self, other):
        if self.x < other.x:
            return Direction.EAST
        elif self.x > other.x:
            return Direction.WEST
        elif self.y < other.y:
            return Direction.SOUTH
        elif self.y > other.y:
            return Direction.NORTH
        raise SameLocations("Locations equal")

    def get_neighbors(self):
        ret = []
        ret.append(self + Direction.NORTH)
        ret.append(self + Direction.SOUTH)
        ret.append(self + Direction.EAST)
        ret.append(self + Direction.WEST)
        return ret
