num_easter_breads = int(input())
best_baker = ""
most_points = 0

for bread in range(num_easter_breads):
    baker_name = input()
    command = input()
    baker_points = 0

    while command != "Stop":
        score = int(command)
        baker_points += score

        command = input()

    print(f"{baker_name} has {baker_points} points.")

    if most_points < baker_points:
        most_points = baker_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{best_baker} won competition with {most_points} points!")
