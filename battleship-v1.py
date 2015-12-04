from random import randint

# possible additional features:
# bigger board, more turns
# multiple battleships
# battleships of different sizes
# multiple players
# track statistics, offer rematches

BOARD_SIZE = 10
TURNS = 5

board = []

for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    print ""
    for row in board:
        print " ".join(row)
    print ""

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

print "\n\n\nLet's play Battleship!"
raw_input("\nPress enter to continue")
print "Here's what the board looks like..."
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row, ship_col

for turn in range(TURNS):
    print "Turn # %d of %d" % (turn + 1, TURNS)
    guess_column = int(raw_input("Guess Column: "))
    guess_row = int(raw_input("Guess Row: "))

    if (guess_column == ship_col) and (guess_row == ship_row):
        print "\n\nCongratulations! You sunk the battleship!"
        break
    else:
        if (guess_row < 1 or guess_row > BOARD_SIZE) or (guess_column < 1 or guess_column > BOARD_SIZE):
            print "\n\nOops, that's not even in the ocean."
        elif(board[guess_row][guess_column] == "X"):
            print "\n\nYou guessed that one already."
        else:
            print "You missed!"
            board[guess_row - 1][guess_column - 1] = "X"
            if turn == (TURNS - 1):
                print "Game Over. The battleship was at row %d column %d\n" % (ship_row, ship_col)
                break
        print_board(board)
