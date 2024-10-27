import numpy as np

# Constants for the players
PLAYER_X = 'X'  # Human player
PLAYER_O = 'O'  # AI player

def create_board():
    """Create an empty Tic-Tac-Toe board."""
    return np.full((3, 3), ' ')

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_winner(board):
    """Check for a winner. Return 'X', 'O', or None."""

    # row
    for row in board:
        # board[0] --> 1st row 

        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # col
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    # other diagonal
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None  # No winner yet

def is_draw(board):  
    """Check for a draw condition."""
    return ' ' not in board



def Minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move."""
    winner = check_winner(board)
    if winner == PLAYER_O:
        return 1  # AI wins
    if winner == PLAYER_X:
        return -1  # Human wins
    if is_draw(board):
        return 0  # Draw
 
    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = PLAYER_O
                    best_score = max(best_score , Minimax(board,depth+1,False))
                    board[i][j] = " "
        return best_score
        
    else:
            best_score = float('inf')
            for i in range(3):
              for j in range(3):
                if board[i][j] == " " :
                    board[i][j] = PLAYER_X
                    best_score = max(best_score , Minimax(board,depth+1,True))
                    board[i][j] = " "
            return best_score
        

def best_move(board):
    """Find the best move for the AI player using Minimax."""
    move = (-1, -1)
    best_value = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_O
                move_value = Minimax(board, 0, False)
                # print(move_value)
                board[i][j] = ' '
                if move_value > best_value: 
                    best_value = move_value
                    move = (i, j)
    return move

def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = create_board()
    while True:
        print_board(board)

        # Player's turn
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == ' ':
                    board[row][col] = PLAYER_X
                    break
                else:
                    print("This cell is already taken! Choose another.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter row and column as 0, 1, or 2.")

        if check_winner(board):
            print_board(board)
            print(f"Player {PLAYER_X} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        if check_winner(board):
            print_board(board)
            print(f"Player {PLAYER_O} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
