version = list(map(int, input().split(".")))

for number in range(len(version) - 1, - 1, -1):
    if number == 0:
        break
    version[number] += 1
    if version[number] > 9:
        version[number] = 0
        version[number - 1] += 1
        if version[number - 1] <= 9:
            break
    else:
        break

new_version = list(map(str, version))
print(".".join(new_version))
