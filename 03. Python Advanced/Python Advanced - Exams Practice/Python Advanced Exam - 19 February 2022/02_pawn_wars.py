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

white_possible_moves = [-1, 0]
black_possible_moves = [1, 0]
white_captures = [[-1, -1], [-1, 1]]
black_captures = [[1, -1], [1, 1]]

turns = 0
current_player = None

while True:

    if turns % 2 == 0:
        current_player = "White"
        player_pos = pawns_positions[current_player]

        white_to_capture_left = [player_pos[0] + white_captures[0][0], player_pos[1] + white_captures[0][1]]
        white_to_capture_right = [player_pos[0] + white_captures[1][0], player_pos[1] + white_captures[1][1]]

        if white_to_capture_left[1] in range(size):
            if chess_board[player_pos[0] + white_captures[0][0]][player_pos[1] + white_captures[0][1]] == "b":
                player_pos = [player_pos[0] + white_captures[0][0], player_pos[1] + white_captures[0][1]]
                print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
                exit()

        if white_to_capture_right[1] in range(size):
            if chess_board[player_pos[0] + white_captures[1][0]][player_pos[1] + white_captures[1][1]] == "b":
                player_pos = [player_pos[0] + white_captures[1][0], player_pos[1] + white_captures[1][1]]
                print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
                exit()

        next_move = [player_pos[0] + white_possible_moves[0], player_pos[1] + white_possible_moves[1]]

        if next_move[0] == size - size:
            player_pos = next_move
            print(f"Game over! {current_player} pawn is promoted to a queen at {output_pos[player_pos[0]][player_pos[1]]}.")
            exit()
        else:
            chess_board[player_pos[0]][player_pos[1]] = "-"
            chess_board[next_move[0]][next_move[1]] = "w"
            pawns_positions[current_player] = next_move

    else:
        current_player = "Black"
        player_pos = pawns_positions[current_player]

        black_to_capture_left = [player_pos[0] + black_captures[0][0], player_pos[1] + black_captures[0][1]]
        black_to_capture_right = [player_pos[0] + black_captures[1][0], player_pos[1] + black_captures[1][1]]

        if black_to_capture_left[1] in range(size):
            if chess_board[player_pos[0] + black_captures[0][0]][player_pos[1] + black_captures[0][1]] == "w":
                player_pos = [player_pos[0] + black_captures[0][0], player_pos[1] + black_captures[0][1]]
                print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
                exit()

        if black_to_capture_right[1] in range(size):
            if chess_board[player_pos[0] + black_captures[1][0]][player_pos[1] + black_captures[1][1]] == "w":
                player_pos = [player_pos[0] + black_captures[1][0], player_pos[1] + black_captures[1][1]]
                print(f"Game over! {current_player} win, capture on {output_pos[player_pos[0]][player_pos[1]]}.")
                exit()

        next_move = [player_pos[0] + black_possible_moves[0], player_pos[1] + black_possible_moves[1]]

        if next_move[0] == size - 1:
            player_pos = next_move
            print(f"Game over! {current_player} pawn is promoted to a queen at {output_pos[player_pos[0]][player_pos[1]]}.")
            exit()
        else:
            chess_board[player_pos[0]][player_pos[1]] = "-"
            chess_board[next_move[0]][next_move[1]] = "b"
            pawns_positions[current_player] = next_move

    turns += 1
