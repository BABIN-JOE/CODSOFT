# Board Representation

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax Algorithm

def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return 10 if row[0] == 'O' else -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'O' else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'O' else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    
# Game Logic

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def is_winner(board, player):
    return evaluate(board) == (10 if player == 'O' else -10)

# User Interface

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'
    turn = 'X'  # X always goes first

    while is_moves_left(board):
        if turn == human_player:
            print_board(board)
            valid_move = False
            while not valid_move:
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        board[row][col] = human_player
                        valid_move = True
                    else:
                        print("This move is not valid, cell already occupied. Try again.")
                else:
                    print("Invalid input, please enter a row and column between 0 and 2.")
                
            if is_winner(board, human_player):
                print_board(board)
                print("Human wins!")
                return
            turn = ai_player
        else:
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = ai_player
            if is_winner(board, ai_player):
                print_board(board)
                print("AI wins!")
                return
            turn = human_player

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
