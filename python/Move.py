##
#
#
#
#
#
#

from Location import Location
from Direction import Direction
from Exceptions import SameLocations
from BoardLocations import KING_TILES


class Move:
    def __init__(self, start_loc, end_loc):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.max_x = 6
        self.max_y = 6
        self.min_x = 0
        self.min_y = 0

    def is_valid(self):
        ret_valid = True
        try:
            self.start_loc.calc_direction_to(self.end_loc)
        except SameLocations:
            ret_valid = False
        if self.start_loc.x != self.end_loc.x and \
           self.start_loc.y != self.end_loc.y:
            ret_valid = False
        if self.start_loc.x < self.min_x or self.start_loc.x > self.max_x or \
           self.start_loc.y < self.min_y or self.start_loc.y > self.max_y:
            ret_valid = False
        if self.end_loc.x < self.min_x or self.end_loc.x > self.max_x or \
           self.end_loc.y < self.min_y or self.end_loc.y > self.max_y:
            ret_valid = False
        return ret_valid
    
    def is_end_king_tile(self):
        return self.end_loc in KING_TILES