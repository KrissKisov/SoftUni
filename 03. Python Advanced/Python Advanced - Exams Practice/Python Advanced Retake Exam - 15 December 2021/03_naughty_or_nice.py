def naughty_or_nice_list(kids, *args, **kwargs):
    santa_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for info in args:
        number, kid_type = info.split("-")
        number = int(number)
        matches = []
        to_remove = []
        for kid_info in kids:
            num, kid_name = kid_info

            if number == num:
                matches.append(kid_info[1])
                to_remove.append(kid_info)

        if len(matches) == 1:
            santa_dict[kid_type].append(matches[0])
            kids.remove(to_remove[0])

    for name, type_of_kid in kwargs.items():

        matched_names = []
        kid_to_remove = []
        for number, name_of_kid in kids:

            if name == name_of_kid:
                matched_names.append(name_of_kid)
                kid_to_remove.append((number, name_of_kid))

        if len(matched_names) == 1:
            santa_dict[type_of_kid].append(matched_names[0])
            kids.remove(kid_to_remove[0])

    for _, kid in kids:
        santa_dict["Not found"].append(kid)

    output = ""
    for key, values in santa_dict.items():
        if values:
            output += ''.join(f"{key}: {', '.join(values)}\n")

    return output


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
