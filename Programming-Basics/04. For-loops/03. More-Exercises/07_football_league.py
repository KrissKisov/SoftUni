stadium_capacity = int(input())
total_fans = int(input())
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0
for fan in range(total_fans):
    sector = input()  # "A", "B", "V" и "G"
    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    else:
        sector_G += 1

percent_A = sector_A / total_fans * 100
percent_B = sector_B / total_fans * 100
percent_V = sector_V / total_fans * 100
percent_G = sector_G / total_fans * 100
percent_total_fans = total_fans / stadium_capacity * 100
print(f"{percent_A :.2f}%")
print(f"{percent_B :.2f}%")
print(f"{percent_V :.2f}%")
print(f"{percent_G :.2f}%")
print(f"{percent_total_fans :.2f}%")
