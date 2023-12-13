notes = []

command = input().split("-")
while command[0] != "End":
    notes.append(command)

    command = input().split("-")

importance = sorted(notes, key=lambda note: int(note[0]))
result = [note[1] for note in importance]
print(result)
