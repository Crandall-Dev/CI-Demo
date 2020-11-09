"""
"""

from enum import Enum
import logging

from Location import Location
from Exceptions import NotAPiece


class PieceType(Enum):
    UNKNOWN = 0
    KING = 1
    ATTACKER = 2
    DEFENDER = 3


class Piece(object):
    """ """
    piece_count = 0

    def __init__(self, x=-1, y=-1, location=None):
        self.id = Piece.piece_count     # Save my ID
        Piece.piece_count += 1          # Increment for next piece

        self._log = logging.getLogger(name=__class__.__name__ + str(self.id))  # noqa: F821, E501
        self.symbol = "p"
        if location:
            self.location = location
        else:
            self.location = Location(x=x, y=y)
        self.type = PieceType.UNKNOWN

    def get_terminal_string(self):
        return self.symbol

    def __str__(self):
        return "{0} {1} ({2}) @ {3}".format(__class__.__name__,   # noqa: F821
                                            self.symbol,
                                            str(self.id),
                                            str(self.location))

    def get_location(self):
        return self.location

    def set_location(self, new_location):
        self.location = new_location

    def is_king(self):
        return self.type == PieceType.KING

    def is_enemy(self, other):
        if not isinstance(other, Piece):
            raise NotAPiece("Checking enemey is not a piece but a: " +
                            str(other))

        if self.type in [PieceType.KING, PieceType.DEFENDER]:
            return other.type is PieceType.ATTACKER
        elif self.type is PieceType.ATTACKER:
            return other.type in [PieceType.KING, PieceType.DEFENDER]

    def to_binary(self):
        return "err"


class King(Piece):
    def __init__(self, x=-1, y=-1, location=None):
        super().__init__(x=x, y=y, location=location)
        self.symbol = chr(0x2654)           # White king in unicode
        self.type = PieceType.KING

    def to_binary(self):
        return "{0:03b}{1:03b}".format(self.location.x, self.location.y)


class Attacker(Piece):
    def __init__(self, x=-1, y=-1, location=None):
        super().__init__(x=x, y=y, location=location)
        self.symbol = chr(0x265F)           # Black pawn in unicode
        self.type = PieceType.ATTACKER

    def to_binary(self):
        return "11"


class Defender(Piece):
    def __init__(self, x=-1, y=-1, location=None):
        super().__init__(x=x, y=y, location=location)
        self.symbol = chr(0x2659)           # White pawn in Unicode
        self.type = PieceType.DEFENDER

    def to_binary(self):
        return "10"


class Pieces(object):
    """ Container for all pieces used in play """
    def __init__(self):
        self._pieces = []           # All pieces
        self.king = None
        self.attackers = []
        self.defenders = []
        self.captured = []

    def add_piece(self, new_piece):
        self._pieces.append(new_piece)              # Add to list of all pieces
        if(new_piece.type == PieceType.KING):
            self.king = new_piece
        elif(new_piece.type == PieceType.ATTACKER):
            self.attackers.append(new_piece)
        elif(new_piece.type == PieceType.DEFENDER):
            self.defenders.append(new_piece)

    def get_pieces(self):
        return self._pieces

    def get_king(self):
        return self.king

    def get_piece_at(self, location):
        # TODO - replace with dictionary lookup!
        for piece in self.attackers:
            if piece.get_location() == location:
                return piece
        for piece in self.defenders:
            if piece.get_location() == location:
                return piece
        if self.king.get_location() == location:
            return self.king
        return None

    def is_piece_at(self, location):
        return self.get_piece_at(location) is not None

    def dump_pieces(self):
        for piece in self._pieces:
            print(piece)

    def move_piece(self, moving_piece, new_location):
        moving_piece.set_location(new_location)
