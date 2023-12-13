usernames = input().split(", ")
for username in usernames:
    if len(username) in range(3, 16 + 1):
        for character in username:
            if not (character.isalnum() or character == "-" or character == "_"):
                break
            if " " in username:
                break
        else:
            print(username)
