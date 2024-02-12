from collections import deque


food_portions = [int(x) for x in input().split(", ")]
stamina_queue = deque([int(x) for x in input().split(", ")])

days = 7
mountain_peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
conquered_peaks = deque()

for day in range(1, days + 1):

    if not mountain_peaks:
        break

    food = food_portions.pop()
    daily_stamina = stamina_queue.popleft()
    result = food + daily_stamina
    current_peak_name, peak_difficulty = mountain_peaks[0]

    if result >= peak_difficulty:
        conquered_peaks.append(current_peak_name)
        mountain_peaks.popleft()

if not mountain_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks: ")
    print('\n'.join(conquered_peaks))
