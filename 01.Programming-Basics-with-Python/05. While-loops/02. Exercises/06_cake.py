# cake_width = int(input())
# cake_length = int(input())
#
# total_pieces = cake_width * cake_length
# pieces_taken = 0
# command = input()
# while command != "STOP":
#     current_pieces = int(command)
#     pieces_taken += current_pieces
#     if pieces_taken >= total_pieces:
#         break
#     command = input()
#
# if command == "STOP":
#     print(f"{total_pieces - pieces_taken} pieces are left.")
# else:
#     print(f"No more cake left! You need {pieces_taken - total_pieces} pieces more.")

# cake_width = int(input())
# cake_length = int(input())
#
# total_pieces = cake_width * cake_length
# command = input()
# while command != "STOP":
#     current_pieces = int(command)
#     total_pieces -= current_pieces
#     if total_pieces <= 0:
#         break
#     command = input()
#
# if command == "STOP":
#     print(f"{total_pieces} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(total_pieces)} pieces more.")

cake_width = int(input())
cake_length = int(input())

total_pieces = cake_width * cake_length

while total_pieces >= 0:
    command = input()
    if command == "STOP":
        break
    current_pieces = int(command)
    total_pieces -= current_pieces

# if command == "STOP":  # Code not fully OK on this line.
#     print(f"{total_pieces} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
if total_pieces <= 0:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")
