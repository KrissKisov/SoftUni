names = input().split(", ")
names.sort(key=lambda x: (-len(x), x))
print(names)

# names = input().split(", ")
# sorted_names = sorted(names, key=lambda x: (-len(x), x))
# print(sorted_names)

# names = input().split(", ")
# print(sorted(names,key=lambda x: (-len(x), x)))
