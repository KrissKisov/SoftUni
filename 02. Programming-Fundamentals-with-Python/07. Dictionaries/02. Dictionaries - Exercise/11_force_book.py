sides = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_exist = False
        if force_side not in sides.keys():
            sides[force_side] = []
        for value in sides.values():
            if force_user in value:
                force_user_exist = True
                break
        if not force_user_exist:
            sides[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in sides.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in sides.keys():
            sides[force_side] = []
        sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, users in sides.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
