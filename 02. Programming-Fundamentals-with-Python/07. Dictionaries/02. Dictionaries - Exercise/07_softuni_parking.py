number = int(input())
registered_users = {}

for i in range(number):
    info = input().split()
    action = info[0]
    username = info[1]

    if action == "register":
        license_plate_number = info[2]
        if username in registered_users.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            registered_users.__delitem__(username)
            print(f"{username} unregistered successfully")

for username, license_plate_number in registered_users.items():
    print(f"{username} => {license_plate_number}")
