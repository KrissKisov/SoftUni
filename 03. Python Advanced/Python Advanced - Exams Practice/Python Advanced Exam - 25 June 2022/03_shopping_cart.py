def shopping_cart(*args):
    max_cart = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    for data in args:
        if data == "Stop":
            break

        meal, product = data

        if product not in cart[meal] and len(cart[meal]) < max_cart[meal]:
            cart[meal].append(product)

    cart = {k: sorted(v) for k, v in cart.items()}
    cart = dict(sorted(cart.items(), key=lambda x: (-len(x[-1]), x[0])))

    output = ""

    for key, values in cart.items():
        output += f"{key}:\n"

        for value in values:
            output += f" - {value}\n"

    if not any(cart.values()):
        return "No products in the cart!"

    return output


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
