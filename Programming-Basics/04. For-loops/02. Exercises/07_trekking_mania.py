groups_count = int(input())

musalla_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for _ in range(groups_count):
    climbers_count = int(input())
    total_climbers += climbers_count
    if climbers_count <= 5:
        musalla_climbers += climbers_count
    elif 6 <= climbers_count <= 12:
        mont_blanc_climbers += climbers_count
    elif 13 <= climbers_count <= 25:
        kilimanjaro_climbers += climbers_count
    elif 26 <= climbers_count <= 40:
        k2_climbers += climbers_count
    elif climbers_count >= 41:
        everest_climbers += climbers_count

musalla_climbers_percent = musalla_climbers / total_climbers * 100
mont_blanc_climbers_percent = mont_blanc_climbers / total_climbers * 100
kilimanjaro_climbers_percent = kilimanjaro_climbers / total_climbers * 100
k2_climbers_percent = k2_climbers / total_climbers * 100
everest_climbers_percent = everest_climbers / total_climbers * 100
print(f"{musalla_climbers_percent :.2f}%")
print(f"{mont_blanc_climbers_percent :.2f}%")
print(f"{kilimanjaro_climbers_percent :.2f}%")
print(f"{k2_climbers_percent :.2f}%")
print(f"{everest_climbers_percent :.2f}%")
