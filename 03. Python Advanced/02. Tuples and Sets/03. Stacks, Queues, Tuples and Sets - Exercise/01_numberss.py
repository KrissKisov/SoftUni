first_integers = set(int(x) for x in input().split())
second_integers = set(int(x) for x in input().split())

commands = {
    "Add First": lambda a: [first_integers.add(int(x)) for x in a],
    "Add Second": lambda a: [second_integers.add(int(x)) for x in a],
    "Remove First": lambda a: [first_integers.discard(int(x)) for x in a],
    "Remove Second": lambda a: [second_integers.discard(int(x)) for x in a],
    "Check Subset": lambda a: print(first_integers.issubset(second_integers) or second_integers.issubset(first_integers)),
}

for _ in range(int(input())):
    first_part, second_part, *nums = input().split()
    command = first_part + " " + second_part

    commands[command](nums)

print(*sorted(first_integers), sep=", ")
print(*sorted(second_integers), sep=", ")
