n = int(input())

# print("+ " + (n - 2) * "- " + "+")
# for _ in range(1, n - 1):
#     print("| " + (n - 2) * "- " + "|")
# print("+ " + (n - 2) * "- " + "+")
for row in range(1, n + 1):
    if row == 1 or row == n:
        print("+ " + (n - 2) * "- " + "+")
    else:
        print("| " + (n - 2) * "- " + "|")
