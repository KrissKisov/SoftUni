def get_player(current_turn, *players):
    for ind, key in enumerate(players):
        if ind % 2 == current_turn % 2:
            return key


def to_capture(current_pos, matrix, *captures):
    for capture in captures:
        if current_pos[1] + capture[1] in range(len(matrix)):
            pos_matched = current_pos[0] + capture[0], current_pos[1] + capture[1]
            if matrix[pos_matched[0]][pos_matched[1]] != "-":
                return pos_matched


def check_for_promotion(position, number):
    if position[0] == 0:
        return True
    elif position[0] == number - 1:
        return True


size = 8
pawns_positions = {
    "White": [],
    "Black": [],
}
chess_board = []

for row in range(size):
    line = input().split()
    chess_board.append(line)

    if "w" in line:
        pawns_positions["White"] = [row, line.index("w")]

    if "b" in line:
        pawns_positions["Black"] = [row, line.index("b")]

output_pos = []
for i in range(size - 1, -1, -1):
    output_row = []

    for j in range(size):
        output_row.append(f"{(chr(ord('a') + j))}{i + 1}")

    output_pos.append(output_row)

possible_moves = {"White": [-1, 0], "Black": [1, 0]}
possible_captures = {"White": ((-1, -1), (-1, 1)), "Black": ((1, -1), (1, 1)), }

turn = 0
current_player = None

while True:

    player = get_player(turn, *pawns_positions)
    player_pos = pawns_positions[player]

    capture_at = to_capture(player_pos, chess_board, *possible_captures[player])
    if capture_at:
        print(f"Game over! {player} win, capture on {output_pos[capture_at[0]][capture_at[1]]}.")
        exit()

    next_pos = [player_pos[0] + possible_moves[player][0], player_pos[1] + possible_moves[player][1]]

    promotion = check_for_promotion(next_pos, size)
    if promotion:
        print(f"Game over! {player} pawn is promoted to a queen at {output_pos[next_pos[0]][next_pos[1]]}.")
        exit()

    pawns_positions[player] = next_pos
    player_sign = chess_board[player_pos[0]][player_pos[1]]
    chess_board[player_pos[0]][player_pos[1]] = "-"
    chess_board[next_pos[0]][next_pos[1]] = player_sign

    turn += 1

#
#
# size = 8
# pawns_positions = {
#     "White": [],
#     "Black": [],
# }
# chess_board = []
#
# for row in range(size):
#     line = input().split()
#     chess_board.append(line)
#
#     if "w" in line:
#         pawns_positions["White"] = [row, line.index("w")]
#
#     if "b" in line:
#         pawns_positions["Black"] = [row, line.index("b")]
#
# output_pos = []
# for i in range(size - 1, -1, -1):
#     output_row = []
#     for j in range(size):
#         output_row.append(f"{(chr(ord('a') + j))}{i + 1}")
#
#     output_pos.append(output_row)
#
# white_possible_moves = [-1, 0]
# black_possible_moves = [1, 0]
# white_captures = [[-1, -1], [-1, 1]]
# black_captures = [[1, -1], [1, 1]]
#
# turns = 0
# current_player = None
#
# while True:
#
#     if turns % 2 == 0:
#         current_player = "White"
#         player_pos = pawns_positions[current_player]
#
#         white_to_capture_left = [player_pos[0] + white_captures[0][0], player_pos[1] + white_captures[0][1]]
#         white_to_capture_right = [player_pos[0] + white_captures[1][0], player_pos[1] + white_captures[1][1]]
#
#         if white_to_capture_left[1] in range(size):
#             if chess_board[player_pos[0] + white_captures[0][0]][player_pos[1] + white_captures[0][1]] == "b":
#                 player_pos = [player_pos[0] + white_captures[0][0], player_pos[1] + white_captures[0][1]]
#                 print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
#                 exit()
#
#         if white_to_capture_right[1] in range(size):
#             if chess_board[player_pos[0] + white_captures[1][0]][player_pos[1] + white_captures[1][1]] == "b":
#                 player_pos = [player_pos[0] + white_captures[1][0], player_pos[1] + white_captures[1][1]]
#                 print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
#                 exit()
#
#         next_move = [player_pos[0] + white_possible_moves[0], player_pos[1] + white_possible_moves[1]]
#
#         if next_move[0] == size - size:
#             player_pos = next_move
#             print(f"Game over! {current_player} pawn is promoted to a queen at {output_pos[player_pos[0]][player_pos[1]]}.")
#             exit()
#         else:
#             chess_board[player_pos[0]][player_pos[1]] = "-"
#             chess_board[next_move[0]][next_move[1]] = "w"
#             pawns_positions[current_player] = next_move
#
#     else:
#         current_player = "Black"
#         player_pos = pawns_positions[current_player]
#
#         black_to_capture_left = [player_pos[0] + black_captures[0][0], player_pos[1] + black_captures[0][1]]
#         black_to_capture_right = [player_pos[0] + black_captures[1][0], player_pos[1] + black_captures[1][1]]
#
#         if black_to_capture_left[1] in range(size):
#             if chess_board[player_pos[0] + black_captures[0][0]][player_pos[1] + black_captures[0][1]] == "w":
#                 player_pos = [player_pos[0] + black_captures[0][0], player_pos[1] + black_captures[0][1]]
#                 print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
#                 exit()
#
#         if black_to_capture_right[1] in range(size):
#             if chess_board[player_pos[0] + black_captures[1][0]][player_pos[1] + black_captures[1][1]] == "w":
#                 player_pos = [player_pos[0] + black_captures[1][0], player_pos[1] + black_captures[1][1]]
#                 print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
#                 exit()
#
#         next_move = [player_pos[0] + black_possible_moves[0], player_pos[1] + black_possible_moves[1]]
#
#         if next_move[0] == size - 1:
#             player_pos = next_move
#             print(f"Game over! {current_player} pawn is promoted to a queen at {output_pos[player_pos[0]][player_pos[1]]}.")
#             exit()
#         else:
#             chess_board[player_pos[0]][player_pos[1]] = "-"
#             chess_board[next_move[0]][next_move[1]] = "b"
#             pawns_positions[current_player] = next_move
#
#     turns += 1
