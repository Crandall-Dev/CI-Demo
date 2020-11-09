#!/usr/bin/env python3

# from Location import Location, boardIndexLookup
# from Pieces import *
from BoardState import BoardState
# from BoardLocations import WEST_EDGE, NORTH_EDGE
# from Location import Location


print("Testing")

print('*' * 80)


print('*' * 80)
kingStart = '011011'
posStart = '00110000011000000100001111101011110001000000011000001100'
whoseTurn = '1'
padding = '0'
startBoard = kingStart + posStart + whoseTurn + padding
print(startBoard)
# 0110110011000001100000010000111110101111000100000001100000110010

boardState = BoardState()
boardState.from_binary(startBoard)
boardState.dump()
print("# " + "*"*77)

print(boardState.get_terminal_string(indicies=True))

metrics = boardState.generate_metrics()
print(metrics)

quit()

# **
children = boardState.generate_children()
for child in children:
    print(child)
    board = BoardState()
    board.from_binary(child)
    # print(board.get_terminal_string())
print("Children count: " + str(len(children)))

print("# " + "*"*77)
retBoard = boardState.to_binary()
print(retBoard)

print("Done")
