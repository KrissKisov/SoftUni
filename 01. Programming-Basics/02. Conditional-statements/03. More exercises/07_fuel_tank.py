type_fuel = input()
amount_fuel = float(input())

# if amount_fuel >= 25:
#     if type_fuel == "Diesel":
#         print(f"You have enough {type_fuel.lower()}.")
#     elif type_fuel == "Gasoline":
#         print(f"You have enough {type_fuel.lower()}.")
#     elif type_fuel == "Gas":
#         print(f"You have enough {type_fuel.lower()}.")
#     else:
#         print("Invalid fuel!")
# elif amount_fuel < 25:
#     if type_fuel == "Diesel":
#         print(f"Fill your tank with {type_fuel.lower()}!")
#     elif type_fuel == "Gasoline":
#         print(f"Fill your tank with {type_fuel.lower()}!")
#     elif type_fuel == "Gas":
#         print(f"Fill your tank with {type_fuel.lower()}!")
#     else:
#         print("Invalid fuel!")

# if type_fuel == "Diesel":
#     if amount_fuel >= 25:
#         print(f"You have enough {type_fuel.lower()}.")
#     else:
#         print(f"Fill your tank with {type_fuel.lower()}!")
# elif type_fuel == "Gasoline":
#     if amount_fuel >= 25:
#         print(f"You have enough {type_fuel.lower()}.")
#     else:
#         print(f"Fill your tank with {type_fuel.lower()}!")
# elif type_fuel == "Gas":
#     if amount_fuel >= 25:
#         print(f"You have enough {type_fuel.lower()}.")
#     else:
#         print(f"Fill your tank with {type_fuel.lower()}!")
# else:
#     print("Invalid fuel!")
if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    if amount_fuel >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print("Invalid fuel!")
