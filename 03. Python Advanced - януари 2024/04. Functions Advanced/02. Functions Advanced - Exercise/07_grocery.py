def grocery_store(**product_info):
    products = dict(sorted(product_info.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    return '\n'.join(f"{x}: {y}" for x, y in products.items())

    # products = sorted(product_info.items(), key=lambda x: x[0])  # Sort by product name in ascending order
    # products.sort(key=lambda x: len(x[0]), reverse=True)  # Then sort by name length in descending order
    # products.sort(key=lambda x: x[1], reverse=True)  # Finally, sort by quantity in descending order
    #
    # return '\n'.join(f"{x}: {y}" for x, y in products)


# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
# print()
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))
