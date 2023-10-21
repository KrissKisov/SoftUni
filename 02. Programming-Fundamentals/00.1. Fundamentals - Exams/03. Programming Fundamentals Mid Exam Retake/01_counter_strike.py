# energy = int(input())
# command = input()
# battles_count = 0
# not_enough_energy = False
# while command != "End of battle":
#     distance = int(command)
#     if energy < distance:
#         not_enough_energy = True
#         break
#     battles_count += 1
#     energy -= distance
#     if battles_count % 3 == 0:
#         energy += battles_count
#
#     command = input()
#
# if not_enough_energy:
#     print(f"Not enough energy! Game ends with {battles_count} won battles and {energy} energy")
# else:
#     print(f"Won battles: {battles_count}. Energy left: {energy}")

def third_battle(battles: int) -> bool:
    if battles % 3 == 0:
        return True
    return False


def enough_battle_energy(initial_energy: int,  some_command: str):
    number_of_battles = 0
    while some_command != "End of battle":
        distance = int(some_command)
        if initial_energy < distance:
            return f"Not enough energy! Game ends with {number_of_battles} won battles and {initial_energy} energy"

        number_of_battles += 1
        initial_energy -= distance
        if third_battle(number_of_battles):
            initial_energy += number_of_battles

        some_command = input()
    return f"Won battles: {number_of_battles}. Energy left: {initial_energy}"


energy = int(input())
command = input()

print(enough_battle_energy(energy, command))
