"""
    Custom exceptions for Tafl
"""


class DiagonalMove(Exception):
    pass


class OffBoard(Exception):
    pass


class BlockedMove(Exception):
    pass


class NoPiece(Exception):
    pass


class NotYourPiece(Exception):
    pass


class SameLocations(Exception):
    pass


class CellAlreadyFull(Exception):
    pass


class NotAPiece(Exception):
    pass
