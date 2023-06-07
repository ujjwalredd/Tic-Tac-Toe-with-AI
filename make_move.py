from minmax import minimax, get_empty_cells
import random




# Constants for representing the players and empty cells
EMPTY = '-'
PLAYER = 'X'
COMPUTER = 'O'

def make_move(board, row, col, player):
    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != " ":
        return False
    board[row][col] = player
    return True

# function to make move
def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for cell in get_empty_cells(board):
        row, col = cell
        board[row][col] = "X"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move
