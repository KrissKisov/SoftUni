# rows = int(input())
# field = []
# for current_row in range(rows):
#     current_field = list(map(int, input().split()))
#     field.append(current_field)
# destroyed_ships = 0
# squares = input().split()
# for square in squares:
#     attacked_square = square.split("-")
#     row = int(attacked_square[0])
#     col = int(attacked_square[1])
#     if int(field[row][col]) >= 1:
#         field[row][col] -= 1
#         if field[row][col] == 0:
#             destroyed_ships += 1
#
# print(destroyed_ships)

def destroyed_ships(field_for_battle: list) -> int:
    destroyed = 0
    squares = input().split()
    for square in squares:
        attacked_square = square.split("-")
        row = int(attacked_square[0])
        col = int(attacked_square[1])
        if int(field_for_battle[row][col]) >= 1:
            field_for_battle[row][col] -= 1
            if field_for_battle[row][col] == 0:
                destroyed += 1

    return destroyed


def battle_field(number_of_rows: int) -> list:
    field = []
    for row in range(number_of_rows):
        current_field = list(map(int, input().split()))
        field.append(current_field)
    return field


rows = int(input())
field_of_battle = battle_field(rows)
print(destroyed_ships(field_of_battle))
