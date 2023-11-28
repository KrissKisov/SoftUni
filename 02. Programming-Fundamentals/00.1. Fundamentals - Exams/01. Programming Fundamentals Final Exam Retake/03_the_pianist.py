pieces_dictionary = {}
number_of_pieces = int(input())
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_dictionary[piece] = {"composer": composer, "key": key}

command = input().split("|")
while command[0] != "Stop":
    action = command[0]
    if action == "Add":
        piece_to_add = command[1]
        composer_to_add = command[2]
        key_to_add = command[3]
        if piece_to_add not in pieces_dictionary.keys():
            pieces_dictionary[piece_to_add] = {"composer": composer_to_add, "key": key_to_add}
            print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")
        else:
            print(f"{piece_to_add} is already in the collection!")

    elif action == "Remove":
        piece_to_remove = command[1]
        if piece_to_remove in pieces_dictionary.keys():
            pieces_dictionary.pop(piece_to_remove)
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")

    elif action == "ChangeKey":
        piece_to_amend = command[1]
        key_to_amend = command[2]
        if piece_to_amend in pieces_dictionary.keys():
            pieces_dictionary[piece_to_amend]["key"] = key_to_amend
            print(f"Changed the key of {piece_to_amend} to {key_to_amend}!")
        else:
            print(f"Invalid operation! {piece_to_amend} does not exist in the collection.")

    command = input().split("|")

for piece, piece_info in pieces_dictionary.items():
    print(f"{piece} -> Composer: {piece_info['composer']}, Key: {piece_info['key']}")
