from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe, Chef

engine = create_engine('postgresql+psycopg2://myuser:mypassword@localhost/sqlalchemy_exercise_db')
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)

    session.add(new_recipe)


# # add recipes
# create_recipe(
#     'Spaghetti Carbonara',
#     'Pasta, Eggs, Pancetta, Cheese',
#     'Cook the pasta, mix it with eggs, pancetta, and cheese'
# )
# create_recipe(
#     'Chicken Stir-Fry',
#     'Chicken, Bell Peppers, Soy Sauce, Vegetables',
#     'Stir-fry chicken and vegetables with soy sauce'
# )
# create_recipe(
#     'Caesar Salad',
#     'Romaine Lettuce, Croutons, Caesar Dressing',
#     'Toss lettuce with dressing and top with croutons'
# )

# # Query all recipes
# recipes = session.query(Recipe).all()
#
# # Loop through each recipe and print its details
# for recipe in recipes:
#     print(f"Recipe name: {recipe.name}")


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str):
    # recipe = session.query(Recipe).filter_by(name=name).first()
    # recipe.name = new_name
    # recipe.ingredients = new_ingredients
    # recipe.instructions = new_instructions
    changed_recipe = session.query(Recipe).filter_by(name=name) \
        .update({Recipe.name: new_name, Recipe.ingredients: new_ingredients, Recipe.instructions: new_instructions})

    return changed_recipe


# # Update a recipe by name
# update_recipe_by_name(
#     name="Spaghetti Carbonara",
#     new_name="Carbonara Pasta",
#     new_ingredients="Pasta, Eggs, Guanciale, Cheese",
#     new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
# )
#
# # Query the updated recipe
# updated_recipe = session.query(Recipe).filter_by(name="Carbonara Pasta").first()
#
# # Print the updated recipe details
# print("Updated Recipe Details:")
# print(f"Name: {updated_recipe.name}")
# print(f"Ingredients: {updated_recipe.ingredients}")
# print(f"Instructions: {updated_recipe.instructions}")


@session_decorator(session)
def delete_recipe_by_name(name: str) -> None:
    session.query(Recipe).filter_by(name=name).delete()


# # Delete a recipe by name
# delete_recipe_by_name("Carbonara Pasta")
#
# # Query all recipes
# recipes = session.query(Recipe).all()
#
# # Loop through each recipe and print its details
# for recipe in recipes:
#     print(f"Recipe name: {recipe.name}")


# # v.1
# @session_decorator(session)
# def get_recipes_by_ingredient(ingredient_name: str) -> list:
#     # recipes = session.query(Recipe).filter(Recipe.ingredients.icontains(ingredient_name)).all()
#     recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f'%{ingredient_name}%')).all()
#
#     return [r.name for r in recipes]
#
#
# # Run the function and print the results
# ingredient_to_filter = 'Common ingredient'
# filtered_recipes_names = get_recipes_by_ingredient('Common ingredient')
#
# print(f"Recipes containing {ingredient_to_filter}:")
# for recipe_name in filtered_recipes_names:
#     print(f"Recipe name - {recipe_name}")


# v.2 - need to close session manually at the end
@session_decorator(session, session_autoclose=False)
def get_recipes_by_ingredient(ingredient_name: str) -> list:
    recipes = session.query(Recipe).filter(Recipe.ingredients.icontains(ingredient_name)).all()
    # recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f'%{ingredient_name}%')).all()

    return recipes


# # Run the function and print the results
# ingredient_to_filter = 'Common ingredient'
# filtered_recipes = get_recipes_by_ingredient('Common ingredient')
#
# print(f"Recipes containing {ingredient_to_filter}:")
# print('\n'.join(f"Recipe name - {recipe.name}" for recipe in filtered_recipes))
# session.close()

@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str) -> None:
    first_recipe = session.query(Recipe).filter_by(name=first_recipe_name) \
        .with_for_update().one()

    second_recipe = session.query(Recipe).filter_by(name=second_recipe_name) \
        .with_for_update().one()

    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients


# # Swap recipes ingredients
# swap_recipe_ingredients_by_name("Caesar Salad", "Chicken Stir-Fry")
#
# recipe1 = session.query(Recipe).filter_by(name="Caesar Salad").first()
# recipe2 = session.query(Recipe).filter_by(name="Chicken Stir-Fry").first()
# print(f"Ceaser Salad ingredients {recipe1.ingredients}")
# print(f"Chicken Stir-Fry ingredients {recipe2.ingredients}")


@session_decorator(session)
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str) -> str:
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe and recipe.chef:
        raise Exception(f'Recipe: {recipe_name} already has a related chef')

    chef = session.query(Chef).filter_by(name=chef_name).first()
    if not chef:
        raise Exception(f'Chef: {chef_name} does not exist')

    recipe.chef = chef

    return f"Related recipe {recipe_name} with chef {chef_name}"


# # Create a recipe instance for Bulgarian Musaka
# musaka_recipe = Recipe(
#     name="Musaka",
#     ingredients="Potatoes, Ground Meat, Onions, Eggs, Milk, Cheese, Spices",
#     instructions="Layer potatoes and meat mixture, pour egg and milk mixture on top, bake until golden brown."
# )
#
# # Create a Bulgarian chef instances
# bulgarian_chef1 = Chef(name="Ivan Zvezdev")
# bulgarian_chef2 = Chef(name="Uti Buchvarov")
#
# session.add_all((musaka_recipe, bulgarian_chef1, bulgarian_chef2,))
# session.commit()
#
# print(relate_recipe_with_chef_by_name("Musaka", "Ivan Zvezdev"))
# print(relate_recipe_with_chef_by_name("Musaka", "Chef Uti"))
# print(relate_recipe_with_chef_by_name("Chicken Stir-Fry", "Uti Buchvarov"))


def get_recipes_with_chef() -> str:
    # recipes = session.query(Recipe).all()
    # return '\n'.join(f'Recipe: {r.name} made by chef: {r.chef.name} ' for r in recipes)

    recipes_and_chefs = session.query(Recipe.name, Chef.name) \
        .join(Chef, Recipe.chef).all()

    return '\n'.join(f'Recipe: {recipe_name} made by chef: {chef_name}'
                     for recipe_name, chef_name in recipes_and_chefs)


# # # Delete all objects (recipes and chefs) from the database
# # session.query(Recipe).delete()
# # session.query(Chef).delete()
# # session.commit()
#
# # Create chef instances
# chef1 = Chef(name="Gordon Ramsay")
# chef2 = Chef(name="Julia Child")
# chef3 = Chef(name="Jamie Oliver")
# chef4 = Chef(name="Nigella Lawson")
#
# # Create recipe instances associated with chefs
# recipe1 = Recipe(name="Beef Wellington", ingredients="Beef fillet, Puff pastry, Mushrooms, Foie gras", instructions="Prepare the fillet and encase it in puff pastry.")
# recipe1.chef = chef1
#
# recipe2 = Recipe(name="Boeuf Bourguignon", ingredients="Beef, Red wine, Onions, Carrots", instructions="Slow-cook the beef with red wine and vegetables.")
# recipe2.chef = chef2
#
# recipe3 = Recipe(name="Spaghetti Carbonara", ingredients="Spaghetti, Eggs, Pancetta, Cheese", instructions="Cook pasta, mix ingredients.")
# recipe3.chef = chef3
#
# recipe4 = Recipe(name="Chocolate Cake", ingredients="Chocolate, Flour, Sugar, Eggs", instructions="Bake a delicious chocolate cake.")
# recipe4.chef = chef4
#
# recipe5 = Recipe(name="Chicken Tikka Masala", ingredients="Chicken, Yogurt, Tomatoes, Spices", instructions="Marinate chicken and cook in a creamy tomato sauce.")
# recipe5.chef = chef3
#
# session.add_all([chef1, chef2, chef3, chef4, recipe1, recipe2, recipe3, recipe4, recipe5])
# session.commit()
# print(get_recipes_with_chef())
