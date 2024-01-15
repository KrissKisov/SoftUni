number = int(input())
usernames = {input() for user in range(number)}

print(*usernames, sep="\n")
# print(*{input() for username in range(int(input()))}, sep="\n")
