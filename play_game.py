from make_move import get_best_move, make_move
from check_win import check_winner


# Constants for representing the players and empty cells
EMPTY = '-'
PLAYER = 'X'
COMPUTER = 'O'


# Function to print the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
            print("|", end=" ")
        print("\n-------------")

    
    
# function to play_game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if not make_move(board, row, col, "O"):
            print("Invalid move. Try again.")
            continue

        if check_winner(board) is not None:
            break

        print("AI is thinking...")
        ai_row, ai_col = get_best_move(board)
        make_move(board, ai_row, ai_col, "X")

        if check_winner(board) is not None:
            break

    print_board(board)
    result = check_winner(board)
    if result == "tie":
        print("It's a tie!")
    else:
        print("The winner is", result + "!")