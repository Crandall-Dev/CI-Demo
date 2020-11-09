import unittest

from BoardState import BoardState


class TestBoardState(unittest.TestCase):
    # TODO: Speedup with class variables & a single run of SetUp
    def setUp(self):
        self.initial_bin = '0110110011000001100000010000111110101111000100000001100000110010'    # noqa: E501
        self.board01_bin = '1000010000000011010011100000000001100001000111101100000000000010'    # noqa: E501
        self.board02_bin = '1000100000000001110011100110011000000000011000011000000000000000'    # noqa: E501

        self.initialBoard = BoardState(bin=self.initial_bin)
        self.board01 = BoardState(bin=self.board01_bin)
        self.board02 = BoardState(bin=self.board02_bin)

    def test_Init_ParseReturn(self):
        self.assertEqual(self.initial_bin, self.initialBoard.to_binary())

    def test_B01_ParseReturn(self):
        self.assertEqual(self.board01_bin, self.board01.to_binary())

    def test_B02_ParseReturn(self):
        print("\n" + self.board02.get_terminal_string(indicies=True))
        self.assertEqual(self.board02_bin, self.board02.to_binary())

    def test_Init_WhoseTurn_Attacker(self):
        self.assertTrue(self.initialBoard.is_attacker_turn())

    def test_Init_WhoseTurn_Defender(self):
        self.assertFalse(self.initialBoard.is_defender_turn())

    def test_B02_WhoseTurn_Attacker(self):
        self.assertFalse(self.board02.is_attacker_turn())

    def test_B02_WhoseTurn_Defender(self):
        self.assertTrue(self.board02.is_defender_turn())

if __name__ == '__main__':
    unittest.main()