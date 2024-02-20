user_name = input()
password = input()

inserted_password = input()
while inserted_password != password:
    inserted_password = input()

print(f"Welcome {user_name}!")
