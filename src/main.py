ROWS = 6
COLS = 7
WIN = 4
EMPTY = " "

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(map(str, range(COLS))))
    for row in board:
        print("| " + " | ".join(row) + " |")

def is_valid_move(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY

def make_move(board, col, piece):
    # Check inserts from bottom up
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = piece
            return

def check_win(board, piece):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == piece for i in range(WIN)):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == piece for i in range(WIN)):
                return True

    # Diagonal \
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(WIN)):
                return True

    # Diagonal /
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == piece for i in range(WIN)):
                return True

    return False

def is_full(board):
    return all(cell != ' ' for cell in board[0])

def play_game():
    board = create_board()
    player = 'X'

    while True:
        print_board(board)
        try:
            col = int(input(f"Player {player}, choose a column (0-{COLS - 1}): "))
        except ValueError:
            print("❌ Invalid input. Enter a number.")
            continue

        if not is_valid_move(board, col):
            print("❌ Column full or out of bounds. Try again.")
            continue

        make_move(board, col, player)

        if check_win(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch to the next player
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
