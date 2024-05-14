def cookbook(*args):
    recipes = {}

    for recipe_name, cuisine, ingredients in args:

        if cuisine not in recipes:
            recipes[cuisine] = {}

            if recipe_name not in recipes[cuisine]:
                recipes[cuisine][recipe_name] = ingredients

        recipes[cuisine][recipe_name] = ingredients

    for key, values in recipes.items():
        recipes[key] = dict(sorted(values.items(), key=lambda x: x[0]))

    recipes = dict(sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ""

    for region, info in recipes.items():
        output += f"{region} cuisine contains {len(info)} recipes:\n"

        for name, content in info.items():
            output += f"  * {name} -> Ingredients: {', '.join(content)}\n"

    return output


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
