pairs_count = int(input())

previous_pair = int(input()) + int(input())
difference = 0
for pair in range(1, pairs_count):
    next_pair = int(input()) + int(input())
    if abs(previous_pair - next_pair) == 0:
        difference = 0
    else:
        difference = abs(previous_pair - next_pair)
    previous_pair = next_pair

if difference == 0:
    print(f"Yes, value={previous_pair}")
else:
    print(f"No, maxdiff={difference}")
'''
n = int(input())
current_sum = int(input()) + int(input())

diff_sum = 0

for _ in range(n - 1):
    next_sum = int(input()) + int(input())

    if abs(current_sum - next_sum) > diff_sum:
        diff_sum = abs(current_sum - next_sum)

    current_sum = next_sum

if diff_sum == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={diff_sum}")
'''