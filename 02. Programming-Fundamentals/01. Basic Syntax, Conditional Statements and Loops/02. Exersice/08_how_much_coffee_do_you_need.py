command = input()
coffee_commands = ["coding", "dog", "cat", "movie"]
coffee_counter = 0

while command != "END":
    current_command = command.lower()
    if any(word in current_command for word in coffee_commands):
        if command.islower():
            coffee_counter += 1
        elif command.isupper():
            coffee_counter += 2

    command = input()

if coffee_counter <= 5:
    print(coffee_counter)
else:
    print("You need extra sleep")
