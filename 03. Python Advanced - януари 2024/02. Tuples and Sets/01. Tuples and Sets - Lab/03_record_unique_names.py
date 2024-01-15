number_of_names = int(input())
names = set()

for _ in range(number_of_names):
    names.add(input())

for name in names:
    print(name)
