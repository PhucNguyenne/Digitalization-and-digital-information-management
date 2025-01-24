import numpy as np

def is_valid_move(mat, row, col):
    return mat[row, col] == 99

def make_move(mat, row, col, player):
    mat[row, col] = 'X' if player == 1 else 'O'

def print_matrix(mat):
    for row in mat:
        print(' '.join(str(cell) for cell in row))
    print()  # Thêm dòng trống để dễ nhìn

def check_winner(mat, player_symbol):
    # Kiểm tra hàng và cột
    for i in range(3):
        if all(mat[i, j] == player_symbol for j in range(3)) or all(mat[j, i] == player_symbol for j in range(3)):
            return True
    # Kiểm tra 2 đường chéo
    if all(mat[i, i] == player_symbol for i in range(3)) or all(mat[i, 2 - i] == player_symbol for i in range(3)):
        return True
    return False

def play_game():
    matrix = np.full((3, 3), 99, dtype=object)  # Sửa dtype thành object
    current_player = 1
    moves = 0
    while moves < 9:
        print_matrix(matrix)
        try:
            move = input(f"Player {'X' if current_player == 1 else 'O'}, enter your move (row,col): ")
            row, col = map(int, move.replace('(', '').replace(')', '').split(','))
            if row not in range(3) or col not in range(3):
                print("Invalid input, row and column must be between 0 and 2.")
                continue
            if is_valid_move(matrix, row, col):
                make_move(matrix, row, col, current_player)
                player_symbol = 'X' if current_player == 1 else 'O'
                if check_winner(matrix, player_symbol):
                    print_matrix(matrix)
                    print(f"Player {player_symbol} wins!")
                    return
                current_player = 1 - current_player
                moves += 1
            else:
                print("Cell already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter the move in the format (row,col).")
    print_matrix(matrix)
    print("It's a draw!")

play_game()
