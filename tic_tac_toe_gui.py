import tkinter as tk
from tkinter import messagebox
import copy

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe - AI (Unbeatable)")

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Create buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check winner
def check_winner(b, player):
    for i in range(3):
        if all(b[i][j] == player for j in range(3)) or all(b[j][i] == player for j in range(3)):
            return True
    if all(b[i][i] == player for i in range(3)) or all(b[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check draw
def check_draw(b):
    return all(b[i][j] != " " for i in range(3) for j in range(3))

# Minimax algorithm
def minimax(b, is_max):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif check_draw(b):
        return 0

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "O"
                    score = minimax(b, False)
                    b[i][j] = " "
                    best = max(score, best)
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "X"
                    score = minimax(b, True)
                    b[i][j] = " "
                    best = min(score, best)
        return best

# Get best AI move
def get_best_move():
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Handle button click
def on_click(i, j):
    if board[i][j] != " ":
        return

    board[i][j] = "X"
    buttons[i][j].config(text="X", state="disabled")

    if check_winner(board, "X"):
        messagebox.showinfo("Game Over", "🎉 You (X) win!")
        reset_board()
        return
    if check_draw(board):
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
        reset_board()
        return

    # AI's Turn
    ai_i, ai_j = get_best_move()
    if ai_i != -1:
        board[ai_i][ai_j] = "O"
        buttons[ai_i][ai_j].config(text="O", state="disabled")

    if check_winner(board, "O"):
        messagebox.showinfo("Game Over", "💻 AI (O) wins!")
        reset_board()
    elif check_draw(board):
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
        reset_board()

# Reset board
def reset_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")

# Create GUI grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 32), width=5, height=2,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
