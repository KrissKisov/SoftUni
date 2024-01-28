# def even_odd_filter(**numbers_sets):  # {odd: [1, 2, 3, 4, 10, 5], even: [3, 4, 5, 7, 10, 2, 5, 5, 2]}
#     if "odd" in numbers_sets:
#         numbers_sets["odd"] = [n for n in numbers_sets["odd"] if n % 2 != 0]
#
#     if "even" in numbers_sets:
#         numbers_sets["even"] = [n for n in numbers_sets["even"] if n % 2 == 0]
#
#     return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))

# #The above code should be slightly faster

def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if key == "odd":
            result[key] = [x for x in value if x % 2 != 0]
        elif key == "even":
            result[key] = [x for x in value if x % 2 == 0]

    # return dict(sorted(result.items(), key=lambda kvp: len(kvp[0]), reverse=True))
    return dict(sorted(result.items(), key=lambda kvp: -len(kvp[1])))


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
