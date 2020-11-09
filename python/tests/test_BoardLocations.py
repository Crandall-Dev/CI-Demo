import unittest
from BoardLocations import BoardLocations, THRONE, CORNERS
from BoardLocations import NORTH_EDGE, SOUTH_EDGE, WEST_EDGE, EAST_EDGE
from Location import Location
# from Direction import Direction
from Exceptions import SameLocations


class TestBoardLocations(unittest.TestCase):

    def test_index_of_2_is_3_0(self):
        loc = BoardLocations.gen_from_index(2)
        loc_target = Location(x=3, y=0)
        self.assertEqual(loc, loc_target)

    def test_index_of_36_is_4_5(self):
        loc = BoardLocations.gen_from_index(36)
        loc_target = Location(x=4, y=5)
        self.assertEqual(loc, loc_target)

    def test_index_of_25_is_0_4(self):
        loc = BoardLocations.gen_from_index(25)
        loc_target = Location(x=0, y=4)
        self.assertEqual(loc, loc_target)

    def test_index_of_neg_1_throws_IndexError(self):
        self.assertRaises(IndexError, BoardLocations.gen_from_index, -1)

    def test_index_of_45_throws_IndexError(self):
        self.assertRaises(IndexError, BoardLocations.gen_from_index, 45)

    def test_same_as_other_raises(self):
        loc = Location(x=5, y=10)
        loc2 = Location(x=5, y=10)
        self.assertRaises(SameLocations, loc.calc_direction_to, loc2)


# ** Places only the king can be ******************************************** #
class TestBoardLocations_KingLocs(unittest.TestCase):
    def test_throne_loc(self):
        loc_target = Location(3, 3)
        self.assertEqual(THRONE, loc_target)

    def test_corner_loc_nw(self):
        loc_target = Location(0, 0)
        self.assertTrue(loc_target in CORNERS)

    def test_corner_loc_ne(self):
        loc_target = Location(6, 0)
        self.assertTrue(loc_target in CORNERS)

    def test_corner_loc_sw(self):
        loc_target = Location(0, 6)
        self.assertTrue(loc_target in CORNERS)

    def test_corner_loc_se(self):
        loc_target = Location(6, 6)
        self.assertTrue(loc_target in CORNERS)


# ** Edges of the board ***************************************************** #
class TestBoardLocations_EdgeSets(unittest.TestCase):
    def test_north_edge_left(self):
        loc_target = Location(1, 0)
        self.assertTrue(loc_target in NORTH_EDGE)

    def test_north_edge_right(self):
        loc_target = Location(5, 0)
        self.assertTrue(loc_target in NORTH_EDGE)

    def test_south_edge_left(self):
        loc_target = Location(1, 6)
        self.assertTrue(loc_target in SOUTH_EDGE)

    def test_south_edge_right(self):
        loc_target = Location(5, 6)
        self.assertTrue(loc_target in SOUTH_EDGE)

    def test_west_edge_top(self):
        loc_target = Location(0, 1)
        self.assertTrue(loc_target in WEST_EDGE)

    def test_west_edge_bottom(self):
        loc_target = Location(0, 5)
        self.assertTrue(loc_target in WEST_EDGE)

    def test_east_edge_top(self):
        loc_target = Location(6, 1)
        self.assertTrue(loc_target in EAST_EDGE)

    def test_east_edge_bottom(self):
        loc_target = Location(6, 5)
        self.assertTrue(loc_target in EAST_EDGE)
