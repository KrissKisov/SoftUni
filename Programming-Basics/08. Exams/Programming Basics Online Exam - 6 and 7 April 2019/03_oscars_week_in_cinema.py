# movie = ("A Star Is Born", "Bohemian Rhapsody", "Green Book", "The Favourite")
# type_of_hall = ("normal", "luxury", "ultra luxury")
film = input()
cinema = input()
ticket_count = int(input())
a_star_is_born_normal = 7.50 * ticket_count
a_star_is_born_luxury = 10.50 * ticket_count
a_star_is_born_ultra_luxury = 13.50 * ticket_count
bohemian_rhapsody_normal = 7.35 * ticket_count
bohemian_rhapsody_luxury = 9.45 * ticket_count
bohemian_rhapsody_ultra_luxury = 12.75 * ticket_count
green_book_normal = 8.15 * ticket_count
green_book_luxury = 10.25 * ticket_count
green_book_ultra_luxury = 13.25 * ticket_count
the_favourite_normal = 8.75 * ticket_count
the_favourite_luxury = 11.55 * ticket_count
the_favourite_ultra_luxury = 13.95 * ticket_count

if film == "A Star Is Born":
    if cinema == "normal":
        print(f"{film} -> {a_star_is_born_normal:.2f} lv.")
    elif cinema == "luxury":
        print(f"{film} -> {a_star_is_born_luxury:.2f} lv.")
    # elif cinema == "ultra_luxury":
    else:
        print(f"{film} -> {a_star_is_born_ultra_luxury:.2f} lv.")
elif film == "Bohemian Rhapsody":
    if cinema == "normal":
        print(f"{film} -> {bohemian_rhapsody_normal:.2f} lv.")
    elif cinema == "luxury":
        print(f"{film} -> {bohemian_rhapsody_luxury:.2f} lv.")
    # elif cinema == "ultra_luxury":
    else:
        print(f"{film} -> {bohemian_rhapsody_ultra_luxury:.2f} lv.")
elif film == "Green Book":
    if cinema == "normal":
        print(f"{film} -> {green_book_normal:.2f} lv.")
    elif cinema == "luxury":
        print(f"{film} -> {green_book_luxury:.2f} lv.")
    # elif cinema == "ultra_luxury":
    else:
        print(f"{film} -> {green_book_ultra_luxury:.2f} lv.")
elif film == "The Favourite":
    if cinema == "normal":
        print(f"{film} -> {the_favourite_normal:.2f} lv.")
    elif cinema == "luxury":
        print(f"{film} -> {the_favourite_luxury:.2f} lv.")
    # elif cinema == "ultra_luxury":
    else:
        print(f"{film} -> {the_favourite_ultra_luxury:.2f} lv.")
    # else:
    #     print("wrong")