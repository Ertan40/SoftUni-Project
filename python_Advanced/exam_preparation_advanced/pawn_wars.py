from math import ceil
size = 8
matrix = []
white_row, white_col = 0, 0
black_row, black_col = 0, 0
matrix_bord = []
for bord_row in range(size, 0, -1):
    value = [f'{chr(97 + x)}{bord_row}' for x in range(size)]
    matrix_bord.append(value)
for row in range(size):
    value = input().split()
    matrix.append(value)
    for col in range(size):
        if matrix[row][col] == 'b':
            black_row, black_col = row, col
        elif matrix[row][col] == 'w':
            white_row, white_col = row, col
if not abs(black_col - white_col) == 1:
    if (size - black_row) > white_row:
        print(f"Game over! White pawn is promoted to a queen at {matrix_bord[size - size][white_col]}.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {matrix_bord[size - 1][black_col]}.")
else:
    if abs(black_row - white_row) % 2 == 0:
        print(
            f"Game over! Black win, capture on {matrix_bord[black_row + ceil(abs(black_row - white_row) / 2)][white_col]}.")
    else:
        print(
            f"Game over! White win, capture on {matrix_bord[white_row - ceil(abs(black_row - white_row) / 2)][black_col]}.")

# -------------------------------------- not my solution ----------------------------

# def draw_board_ranks():
#     chess_ranks = []
#     letters = "abcdefgh"
#     for row in range(matrix_size, 0, -1):
#         chess_ranks.append([letters[col] + str(row) for col in range(matrix_size)])
#     return chess_ranks
#
# def find_pawns():
#     black = []
#     white = []
#     for row in range(matrix_size):
#         for col in range(len(matrix[row])):
#             if matrix[row][col] == "b":
#                 black = [row, col]
#             if matrix[row][col] == "w":
#                 white = [row, col]
#     return black, white
#
# def white_pawn_move(row, col):
#     if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix):
#         if "b" == matrix[row - 1][col - 1]:
#             print(f"Game over! White win, capture on {chess_board_ranks[row - 1][col - 1]}.")
#             rules['white'] = True
#     if 0 <= row - 1 < len(matrix) and 0 <= col + 1 < len(matrix):
#         if "b" == matrix[row - 1][col + 1]:
#             print(f"Game over! White win, capture on {chess_board_ranks[row - 1][col + 1]}.")
#             rules['white'] = True
#     if 0 <= row < len(matrix):
#         if not rules['white']:
#             matrix[row][col] = "-"
#             row -= 1
#             matrix[row][col] = "w"
#         if row == 0:
#             print(f"Game over! White pawn is promoted to a queen at {chess_board_ranks[row][col]}.")
#             rules['white'] = True
#     return [row, col]
#
# def black_pawn_move(row, col):
#     if 0 <= row + 1 < len(matrix) and 0 <= col - 1 < len(matrix):
#         if "w" == matrix[row + 1][col - 1]:
#             print(f"Game over! Black win, capture on {chess_board_ranks[row + 1][col - 1]}.")
#             rules['black'] = True
#     if 0 <= row + 1 < len(matrix) and 0 <= col + 1 < len(matrix):
#         if "w" == matrix[row + 1][col + 1]:
#             print(f"Game over! Black win, capture on {chess_board_ranks[row + 1][col + 1]}.")
#             rules['black'] = True
#     if 0 <= row < len(matrix):
#         if not rules['black']:
#             matrix[row][col] = "-"
#             row += 1
#             matrix[row][col] = "b"
#         if row == 7:
#             print(f"Game over! Black pawn is promoted to a queen at {chess_board_ranks[row][col]}.")
#             rules['black'] = True
#     return [row, col]
#
# matrix_size = 8
# chess_board_ranks = draw_board_ranks()
# matrix = [[col for col in input().split()] for row in range(matrix_size)]
# black_pawn, white_pawn = find_pawns()
# take_turns = 1
# rules = {
#     'white': False,
#     'black': False,
# }
# while not rules['white'] and not rules['black']:
#     if take_turns % 2 != 0:
#         white_pawn = white_pawn_move(*white_pawn)
#     elif take_turns % 2 == 0:
#         black_pawn = black_pawn_move(*black_pawn)
#     take_turns += 1
# [print(*matrix[row]) for row in range(matrix_size)]
# print()