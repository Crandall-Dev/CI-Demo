"""
"""

from enum import Enum


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

    @classmethod
    def reverse(cls, dir):
        if dir is Direction.NORTH:
            return Direction.SOUTH
        elif dir is Direction.SOUTH:
            return Direction.NORTH
        elif dir is Direction.EAST:
            return Direction.WEST
        elif dir is Direction.WEST:
            return Direction.EAST

DIRECTIONS = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
