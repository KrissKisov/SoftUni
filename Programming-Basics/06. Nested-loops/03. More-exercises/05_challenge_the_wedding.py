men = int(input())
women = int(input())
tables = int(input())
couple = 0
for man in range(1, men + 1):
    for woman in range(1, women + 1):
        couple += 1
        if couple <= tables:
            print(f"({man} <-> {woman})", end=" ")
        else:
            break
