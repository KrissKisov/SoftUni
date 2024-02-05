def concatenate(*args, **kwargs):
    given_string = "".join(args)

    for key, value in kwargs.items():
        if key in given_string:
            given_string = given_string.replace(key, value)

    return given_string


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
