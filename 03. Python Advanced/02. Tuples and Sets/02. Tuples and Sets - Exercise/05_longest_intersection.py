longest_intersection = set()

for _ in range(int(input())):

    first_range, second_range = [[int(x) for x in x.split(",")] for x in input().split("-")]

    first_set = set(range(first_range[0], first_range[-1] + 1))
    second_set = set(range(second_range[0], second_range[-1] + 1))

    intersection = set(first_set.intersection(second_set))

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
