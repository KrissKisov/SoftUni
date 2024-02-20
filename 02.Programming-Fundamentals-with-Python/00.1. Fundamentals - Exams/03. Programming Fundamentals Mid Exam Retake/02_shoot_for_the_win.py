# def index_in_range(index: int, some_list: list) -> bool:
#     if index in range(len(some_list)):
#         return True
#     return False
#
#
# def target_changer(list_with_targets: list, index, value_of_target, target_count) -> list and int:
#     target_count += 1
#     list_with_targets[index] = -1
#     for target in range(len(list_with_targets)):
#         if list_with_targets[target] == -1:
#             continue
#
#         if list_with_targets[target] > value_of_target:
#             list_with_targets[target] -= value_of_target
#         else:
#             list_with_targets[target] += value_of_target
#
#     return list([str(x) for x in list_with_targets]), target_count
#
#
# targets = [int(x) for x in input().split()]
# shot_targets = 0
# targets_at_end = []
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     target_index = int(command)
#     if not index_in_range(target_index, targets):
#         continue
#
#     target_value = targets[target_index]
#     if target_value == -1:
#         continue
#
#     targets_at_end, shot_targets = target_changer(targets, target_index, target_value, shot_targets)
# if len(targets_at_end) == 0:
#     targets = [str(x) for x in targets]
#     print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")
# else:
#     print(f"Shot targets: {shot_targets} -> {' '.join(targets_at_end)}")


targets = [int(x) for x in input().split()]
shot_targets = 0
while True:
    command = input()
    if command == "End":
        break

    target_index = int(command)
    if target_index not in range(len(targets)):
        continue

    target_value = targets[target_index]
    if target_value == -1:
        continue

    shot_targets += 1
    targets[target_index] = -1
    for target in range(len(targets)):
        if targets[target] == -1:
            continue

        if targets[target] > target_value:
            targets[target] -= target_value
        else:
            targets[target] += target_value

targets_at_end = [str(x) for x in targets]
print(f"Shot targets: {shot_targets} -> {' '.join(targets_at_end)}")
