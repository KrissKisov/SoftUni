groups = int(input())

climbers_musala = 0
climbers_mont_blanc = 0
climbers_kilimanjaro = 0
climbers_k2 = 0
climbers_everest = 0
total_climbers = 0
for group in range(groups):
    people = int(input())
    total_climbers += people

    if people <= 5:
        climbers_musala += people
    elif people <= 12:
        climbers_mont_blanc += people
    elif people <= 25:
        climbers_kilimanjaro += people
    elif people <= 40:
        climbers_k2 += people
    else:
        climbers_everest += people

percent_musala = climbers_musala / total_climbers * 100
percent_mont_blanc = climbers_mont_blanc / total_climbers * 100
percent_kilimanjaro = climbers_kilimanjaro / total_climbers * 100
percent_k2 = climbers_k2 / total_climbers * 100
percent_everest = climbers_everest / total_climbers * 100
print(f"{percent_musala :.2f}%")
print(f"{percent_mont_blanc :.2f}%")
print(f"{percent_kilimanjaro :.2f}%")
print(f"{percent_k2 :.2f}%")
print(f"{percent_everest :.2f}%")
