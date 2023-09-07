length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

total_volume = (length * width * height) / 1000
volume_to_fill = total_volume - (total_volume * percentage / 100)

print(volume_to_fill)