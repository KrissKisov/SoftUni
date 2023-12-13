number = int(input())
train = list(map(int, "0" * number))

while True:
    command = input().split()
    if command[0] == "End":
        break

    if command[0] == "add":
        train[-1] += int(command[1])
    elif int(command[1]) not in range(0, number):
        continue
    else:
        if command[0] == "insert":
            train[int(command[1])] += int(command[2])
        elif command[0] == "leave":
            if train[int(command[1])] < int(command[2]):
                continue
            train[int(command[1])] -= int(command[2])

print(train)
