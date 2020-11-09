##
#   A singel game board's state
#
#   @author Aaron S. Crandall <crandall@gonzaga.edu>
#   @copyright 2020
#

from Pieces import Pieces, King, Attacker, Defender
from Location import Location
from Direction import DIRECTIONS
from BoardMetrics import BoardMetrics
from BoardLocations import BoardLocations, KING_TILES


# *************************************************************************** #
class BoardState:
    def __init__(self, bin="", last_move=None):
        self.pieces = Pieces()
        self.whoseTurn = "D"
        self.max_x = 7
        self.max_y = 7
        self.bin_str = bin
        self.last_moved=last_move

        if self.bin_str:
            self.from_binary(self.bin_str)

    # TODO: how can a move know if it's valid without the pieces?
    def resolve_move(self, last_move):
        if not last_move.is_valid():    # There's a smell here
            return
        moved_piece = self.pieces.get_piece_at(last_move.end_loc)
        if not moved_piece:     # No piece at end of move... throw?
            return
        piece_loc = moved_piece.get_location()
        for dir in DIRECTIONS:
            neighbor_loc = piece_loc + dir
            far_neighbor_loc = neighbor_loc + dir

            neighbor_piece = self.pieces.get_piece_at(neighbor_loc)
            if neighbor_piece and moved_piece.is_enemy(neighbor_piece):
                far_neighbor_piece = self.pieces.get_piece_at(far_neighbor_loc)
                if far_neighbor_piece and not moved_piece.is_enemy(far_neighbor_piece):
                    pass
                    # TODO: Capture neighbor piece
               


    # Take in a string of 1's and 0's as passed as a board state
    def from_binary(self, boardBits):
        kingX = int(boardBits[0:3], 2)
        kingY = int(boardBits[3:6], 2)
        self.pieces.add_piece(King(x=kingX, y=kingY))

        locIndex = 0
        strIndex = 6
        while locIndex < 44:
            if boardBits[strIndex] == '1':     # piece found here
                newLoc = BoardLocations.gen_from_index(locIndex)
                if boardBits[strIndex + 1] == '1':
                    self.pieces.add_piece(Attacker(location=newLoc))
                else:
                    self.pieces.add_piece(Defender(location=newLoc))
                strIndex += 1            # advance one for the data payload
            locIndex += 1
            strIndex += 1

        self.whoseTurn = "D"
        if boardBits[-2] == "1":
            self.whoseTurn = "A"

    def is_attacker_turn(self):
        return self.whoseTurn == "A"

    def is_defender_turn(self):
        return self.whoseTurn == "D"

    def dump(self):
        self.pieces.dump_pieces()

    # Emit a string of 1's and 0's as passed as a board state
    def to_binary(self):
        ret = ""
        ret += self.pieces.king.to_binary()
        non_king_piece_count = 0;
        for locIndex in range(44):
            location = BoardLocations.gen_from_index(locIndex)
            piece = self.pieces.get_piece_at(location)
            if piece:
                if piece.is_king():
                    ret += "0"
                else:
                    ret += piece.to_binary()
                    non_king_piece_count += 1
            else:
                ret += "0"

        # Add on zeros for captured pieces as padding
        for i in range(12-non_king_piece_count):
            ret += "0"

        # Add on the bit for whose turn it is
        if self.whoseTurn == "A":
            ret += "1"
        else:
            ret += "0"
        ret += "0"              # Reserved padding bit
        return ret

    # TODO: Change this to functions, geez Crandall
    def gen_child_states(self):
        ret = []
        moveList = None
        realTurn = self.whoseTurn

        if self.whoseTurn == "A":       # Move attackers
            moveList = self.pieces.attackers
            self.whoseTurn = "D"
        else:                           # Move Defenders
            moveList = self.pieces.defenders
            self.whoseTurn = "A"
        for currPiece in moveList:
            start_location = currPiece.get_location()
            startX = start_location.x
            startY = start_location.y
            # print("Startx = {0} , Starty = {1}".format(startX, startY))

            maxX = 7
            minX = -1
            maxY = 7
            minY = -1
            if not currPiece.is_king():
                if startY == 0 or startY == 6:      # corners
                    maxX = 6
                    minX = 0
                if startX == 0 or startX == 6:      # corners
                    maxY = 6
                    minY = 0

            for curr_x in range(startX + 1, maxX):  # move right
                new_loc = Location(x=curr_x, y=startY)
                print(new_loc)
                piece = self.pieces.get_piece_at(new_loc)
                if not piece:
                    currPiece.set_location(new_loc)
                    ret.append(self.to_binary())
                else:
                    break                           # hit another piece
            currPiece.set_location(start_location)

            for curr_x in range(startX - 1, minX, -1):  # move left
                new_loc = Location(x=curr_x, y=startY)
                print(new_loc)
                piece = self.pieces.get_piece_at(new_loc)
                if not piece:
                    currPiece.set_location(new_loc)
                    ret.append(self.to_binary())
                else:
                    break                           # hit another piece
            currPiece.set_location(start_location)

            for curr_y in range(startY - 1, minY, -1):  # move upwards
                new_loc = Location(x=startX, y=curr_y)
                print(new_loc)
                piece = self.pieces.get_piece_at(new_loc)
                if not piece:
                    currPiece.set_location(new_loc)
                    ret.append(self.to_binary())
                else:
                    break                   # hit another piece - stop looping
            currPiece.set_location(start_location)

            for curr_y in range(startY + 1, maxY):  # move downwards
                new_loc = Location(x=startX, y=curr_y)
                print(new_loc)
                piece = self.pieces.get_piece_at(new_loc)
                if not piece:
                    currPiece.set_location(new_loc)
                    ret.append(self.to_binary())
                else:
                    break                   # hit another piece - stop looping
            currPiece.set_location(start_location)

        self.whoseTurn = realTurn
        return ret

    # Create a metrics object from the current board state for heuristics use
    def generate_metrics(self):
        metrics = BoardMetrics()
        metrics.update_metrics(self.pieces)
        return metrics

    # Returns a string representing the board visually for terminal output
    def get_terminal_string(self, indicies=False):
        # pragma: nocover
        ret = ""
        if indicies is True:
            ret += " X "
            for i in range(self.max_x):
                ret += "{:<2}".format(i)
            ret += "\n"
        for y in range(self.max_y):
            if indicies is True:
                if y == 0:
                    ret += "Y "
                else:
                    ret += "  "
            ret += "+-" * self.max_x + "+\n"
            if indicies is True:
                ret += "{:<2}".format(y)
            for x in range(self.max_x):
                currLoc = Location(x=x, y=y)
                piece = self.pieces.get_piece_at(currLoc)
                draw = " "
                if currLoc in KING_TILES:   # Really, a total hack
                    draw = chr(0x2318)
                if piece:
                    draw = piece.get_terminal_string()
                ret += "|" + draw
            ret += "|\n"
        if indicies is True:
            ret += "  "
        ret += "+-" * self.max_x + "+\n"
        return ret
