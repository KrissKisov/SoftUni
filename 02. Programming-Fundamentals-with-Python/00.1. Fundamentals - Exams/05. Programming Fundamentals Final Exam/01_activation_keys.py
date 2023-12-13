raw_activation_key = input()
command = input()
while "Generate" not in command:
    if "Contains" in command:
        substring = command.split(">>>")[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in command:
        start_index = int(command.split(">>>")[2])
        end_index = int(command.split(">>>")[3])
        substring_to_change = raw_activation_key[start_index:end_index]
        if "Upper" in command:
            raw_activation_key = raw_activation_key[:start_index] + substring_to_change.upper() + raw_activation_key[end_index:]
        elif "Lower" in command:
            raw_activation_key = raw_activation_key[:start_index] + substring_to_change.lower() + raw_activation_key[end_index:]

        print(raw_activation_key)

    elif "Slice" in command:
        start = int(command.split(">>>")[1])
        end = int(command.split(">>>")[2])
        raw_activation_key = raw_activation_key[:start] + raw_activation_key[end:]
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")
