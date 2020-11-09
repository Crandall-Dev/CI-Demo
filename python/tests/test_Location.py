import unittest
from Location import Location
from Direction import Direction
from Exceptions import SameLocations


class TestLocation(unittest.TestCase):

    def test_default_x(self):
        loc = Location()
        self.assertEqual(loc.x, -1)

    def test_default_y(self):
        loc = Location()
        self.assertEqual(loc.y, -1)

    def test_equality(self):
        loc = Location(x=5, y=10)
        loc2 = Location(x=5, y=10)
        self.assertEqual(loc, loc2)

    def test_not_equality_x(self):
        loc = Location(x=5, y=10)
        loc2 = Location(x=7, y=10)
        self.assertNotEqual(loc, loc2)

    def test_not_equality_y(self):
        loc = Location(x=5, y=10)
        loc2 = Location(x=5, y=15)
        self.assertNotEqual(loc, loc2)

    def test_go_north(self):
        loc = Location(x=5, y=10)
        loc2 = loc + Direction.NORTH
        locTarget = Location(x=5, y=9)
        self.assertEqual(loc2, locTarget)

    def test_go_south(self):
        loc = Location(x=5, y=10)
        loc2 = loc + Direction.SOUTH
        locTarget = Location(x=5, y=11)
        self.assertEqual(loc2, locTarget)

    def test_go_east(self):
        loc = Location(x=5, y=10)
        loc2 = loc + Direction.EAST
        locTarget = Location(x=6, y=10)
        self.assertEqual(loc2, locTarget)

    def test_go_west(self):
        loc = Location(x=5, y=10)
        loc2 = loc + Direction.WEST
        locTarget = Location(x=4, y=10)
        self.assertEqual(loc2, locTarget)

    def test_same_as_other_raises(self):
        loc = Location(x=5, y=10)
        loc2 = Location(x=5, y=10)
        self.assertRaises(SameLocations, loc.calc_direction_to, loc2)
