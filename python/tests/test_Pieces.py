"""
"""

import unittest
from Pieces import King, Attacker, Defender, PieceType
from Location import Location


class TestKing(unittest.TestCase):
    def setUp(self):
        self.piece = King()

    def test_symbol(self):
        self.assertEqual(self.piece.symbol, chr(0x2654))

    def test_terminal_string(self):
        self.assertEqual(self.piece.get_terminal_string(), chr(0x2654))

    def test_piece_type(self):
        self.assertEqual(self.piece.type, PieceType.KING)

    def test_is_king(self):
        self.assertTrue(self.piece.is_king())

    def test_location(self):
        self.piece.location = Location(x=5, y=10)
        self.assertEqual(self.piece.location, Location(x=5, y=10))

    def test_is_enemy_true(self):
        self.assertTrue(self.piece.is_enemy(Attacker()))

    def test_is_enemy_false(self):
        self.assertFalse(self.piece.is_enemy(Defender()))


class TestAttacker(unittest.TestCase):
    def setUp(self):
        self.piece = Attacker()

    def test_symbol(self):
        self.assertEqual(self.piece.symbol, chr(0x265F))

    def test_terminal_string(self):
        self.assertEqual(self.piece.get_terminal_string(), chr(0x265F))

    def test_piece_type(self):
        self.assertEqual(self.piece.type, PieceType.ATTACKER)

    def test_is_king(self):
        self.assertFalse(self.piece.is_king())

    def test_location(self):
        self.piece.location = Location(x=5, y=10)
        self.assertEqual(self.piece.location, Location(x=5, y=10))

    def test_is_enemy_true(self):
        self.assertTrue(self.piece.is_enemy(Defender()))

    def test_is_enemy_true_king(self):
        self.assertTrue(self.piece.is_enemy(King()))

    def test_is_enemy_false(self):
        self.assertFalse(self.piece.is_enemy(Attacker()))


class TestDefender(unittest.TestCase):
    def setUp(self):
        self.piece = Defender()

    def test_symbol(self):
        self.assertEqual(self.piece.symbol, chr(0x2659))

    def test_terminal_string(self):
        self.assertEqual(self.piece.get_terminal_string(), chr(0x2659))

    def test_piece_type(self):
        self.assertEqual(self.piece.type, PieceType.DEFENDER)

    def test_location(self):
        self.piece.location = Location(x=5, y=10)
        self.assertEqual(self.piece.location, Location(x=5, y=10))

    def test_is_king(self):
        self.assertFalse(self.piece.is_king())

    def test_is_enemy_true(self):
        self.assertTrue(self.piece.is_enemy(Attacker()))

    def test_is_enemy_false_king(self):
        self.assertFalse(self.piece.is_enemy(King()))

    def test_is_enemy_false(self):
        self.assertFalse(self.piece.is_enemy(Defender()))
