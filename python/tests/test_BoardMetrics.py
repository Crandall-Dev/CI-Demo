import unittest

from BoardState import BoardState


class TestBoardMetrics(unittest.TestCase):
    # TODO: Speedup with class variables & a single run of SetUp
    def setUp(self):
        initial_bin = '0110110011000001100000010000111110101111000100000001100000110010'    # noqa: E501
        board01_bin = '1000010000000011010011100000000001100001000111101100000000010'       # noqa: E501

        self.initialBoard = BoardState()
        self.initialBoard.from_binary(initial_bin)
        self.initialBoardMetrics = self.initialBoard.generate_metrics()
        # print(self.initialBoard.get_terminal_string())

        self.board01 = BoardState()
        self.board01.from_binary(board01_bin)
        self.board01Metrics = self.board01.generate_metrics()

        # print(self.board01.get_terminal_string())

    def test_Init_KingOnThrone(self):
        self.assertTrue(self.initialBoardMetrics.throne_occupied)

    def test_B01_KingNotOnThrone(self):
        self.assertFalse(self.board01Metrics.throne_occupied)
