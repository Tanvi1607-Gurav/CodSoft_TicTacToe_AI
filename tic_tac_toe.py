# Step 1: Create and display the board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Step 2: Handle player moves
def player_move(board, player):
    while True:
        try:
            row = int(input(f"{player}'s Turn - Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers from 0 to 2.")

# Step 3: Check winner
def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check rows
            return True
        if all(row[i] == player for row in board):    # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False

# Step 4: Check draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Step 5: Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Step 6: AI's best move
def get_best_move(board):
    best_score = -float('inf')
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Step 7: Full game logic
def play_game():
    board = create_board()
    current_player = "X"
    print_board(board)

    while True:
        if current_player == "X":
            player_move(board, "X")
        else:
            row, col = get_best_move(board)
            board[row][col] = "O"

        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return current_player

        if check_draw(board):
            print("🤝 It's a draw!")
            return "Draw"

        current_player = "O" if current_player == "X" else "X"

# Step 8: Loop with scoreboard
x_wins = 0
o_wins = 0
draws = 0

while True:
    winner = play_game()

    if winner == "X":
        x_wins += 1
    elif winner == "O":
        o_wins += 1
    else:
        draws += 1

    print(f"\n📊 Scoreboard:")
    print(f"Player X Wins: {x_wins}")
    print(f"AI (O) Wins: {o_wins}")
    print(f"Draws: {draws}")

    choice = input("\nDo you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("👋 Thanks for playing!")
        break
