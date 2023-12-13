hours = int(input())
minutes = int(input())

minutes += 15 # minutes = minutes + 15

if minutes > 59:
    hours += 1 # hours = hours + 1
if hours > 23:
    hours = 0

minutes %= 60 # minutes = minutes % 60

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
