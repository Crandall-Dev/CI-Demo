##
#   Little helper factory for making locations
#

from Location import Location

CORNERS = [Location(0, 0), Location(6, 0), Location(0, 6), Location(6, 6)]
THRONE = Location(3, 3)
KING_TILES = [Location(0, 0), Location(6, 0), Location(0, 6),
              Location(6, 6), Location(3, 3)]

NORTH_EDGE = list(map(lambda x: Location(x, 0), range(1, 6)))
SOUTH_EDGE = list(map(lambda x: Location(x, 6), range(1, 6)))
WEST_EDGE = list(map(lambda y: Location(0, y), range(1, 6)))
EAST_EDGE = list(map(lambda y: Location(6, y), range(1, 6)))


# *************************************************************************** #
class BoardLocations:
    def gen_from_index(index):

        boardIndexLookup = [
        (1,0) , (2,0) , (3,0) , (4,0) , (5,0) ,             # noqa: E122, E231, E203, E501
(0,1) , (1,1) , (2,1) , (3,1) , (4,1) , (5,1) , (6,1) ,     # noqa: E122, E231, E203, E501
(0,2) , (1,2) , (2,2) , (3,2) , (4,2) , (5,2) , (6,2) ,     # noqa: E122, E231, E203, E501
(0,3) , (1,3) , (2,3) ,         (4,3) , (5,3) , (6,3) ,     # noqa: E122, E231, E203, E501
(0,4) , (1,4) , (2,4) , (3,4) , (4,4) , (5,4) , (6,4) ,     # noqa: E122, E231, E203, E501
(0,5) , (1,5) , (2,5) , (3,5) , (4,5) , (5,5) , (6,5) ,     # noqa: E122, E231, E203, E501
        (1,6) , (2,6) , (3,6) , (4,6) , (5,6)]              # noqa: E122, E231, E203, E501

        if index < 0 or index >= len(boardIndexLookup):
            raise IndexError("Bounds err for index lookup: {0}".format(index))

        loc_tuple = boardIndexLookup[index]
        loc = Location(x=loc_tuple[0], y=loc_tuple[1])
        return loc

    def is_loc_on_board(loc):
        if loc.x > 0 and loc.x < 7 and loc.y > 0 and loc.y < 7:
            return True
        return False
