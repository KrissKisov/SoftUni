string = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break

    if command[0] == "merge":
        start = int(command[1])
        end = int(command[2])

        if start not in range(len(string)):
            start = 0

        if end not in range(len(string)):
            end = len(string) - 1

        string[start:end + 1] = [''.join(string[start:end + 1])]

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        part_to_split = string[index]
        parts_length = len(part_to_split) // partitions
        split_parts = []

        while len(split_parts) < partitions:

            if len(split_parts) == partitions - 1:
                split_parts.append(part_to_split)
            else:
                split_parts.append(part_to_split[:parts_length])
                part_to_split = part_to_split[parts_length:]

        string[index:index + 1] = split_parts

print(" ".join(string))
