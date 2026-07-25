# Tic-Tac-Toe Game in Python

board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for position in win_positions:
        if all(board[i] == player for i in position):
            return True
    return False

def board_full():
    return " " not in board

current_player = "X"

print("===== TIC-TAC-TOE GAME =====")
print("Board Positions:")
print(" 1 | 2 | 3")
print("---|---|---")
print(" 4 | 5 | 6")
print("---|---|---")
print(" 7 | 8 | 9")

while True:
    display_board()

    try:
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position! Choose between 1 and 9.")
            continue

        if board[move] != " ":
            print("Position already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            display_board()
            print(f"🎉 Player {current_player} Wins!")
            break

        if board_full():
            display_board()
            print("🤝 It's a Draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    except ValueError:
        print("Please enter a valid number.")