from check_win import check_winner


# Constants for representing the players and empty cells
EMPTY = '-'
PLAYER = 'X'
COMPUTER = 'O'


# Function to evaluate the game board
def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

# function to minmax
def minimax(board, depth, maximizing_player):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    result = check_winner(board)
    if result is not None:
        return scores[result]

    if maximizing_player:
        max_score = float("-inf")
        for cell in get_empty_cells(board):
            row, col = cell
            board[row][col] = "X"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_score = max(max_score, score)
        return max_score
    else:
        min_score = float("inf")
        for cell in get_empty_cells(board):
            row, col = cell
            board[row][col] = "O"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_score = min(min_score, score)
        return min_score
