n, m = input().split()

first_set = {input() for _ in range(int(n))}
second_set = {input() for _ in range(int(m))}

# # intersection = first_set.intersection(second_set)
# intersection = first_set & second_set
# print(*intersection, sep="\n")

print(*(first_set & second_set), sep="\n")
