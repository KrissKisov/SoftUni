import os
from typing import List

import django
from django.db.models import Case, When, Value, QuerySet

from main_app.choices import OperationSystemChoice, LaptopBrandChoice, MealTypeChoices, DifficultyChoices, \
    WorkoutTypeChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


# Create and check models
def show_highest_rated_art() -> str:
    art_work = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{art_work.art_name} is the highest-rated art with a {art_work.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create((first_art, second_art))


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    # Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)
    Laptop.objects.filter(brand__in=(
        LaptopBrandChoice.ASUS, LaptopBrandChoice.LENOVO
    )).update(storage=512)


def update_to_16_GB_memory() -> None:
    # Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)
    Laptop.objects.filter(brand__in=(
        LaptopBrandChoice.APPLE, LaptopBrandChoice.DELL, LaptopBrandChoice.ACER
    )).update(memory=16)


def update_operation_systems() -> None:
    # # Laptop.objects.filter(brand="Asus").update(operation_system=OperationSystemChoice.WINDOWS)
    # Laptop.objects.filter(
    #     brand=LaptopBrandChoice.ASUS
    # ).update(operation_system=OperationSystemChoice.WINDOWS)
    # # Laptop.objects.filter(brand="Apple").update(operation_system=OperationSystemChoice.MACOS)
    # Laptop.objects.filter(
    #     brand=LaptopBrandChoice.APPLE
    # ).update(operation_system=OperationSystemChoice.MACOS)
    # # Laptop.objects.filter(brand__in=("Dell", "Acer")).update(operation_system=OperationSystemChoice.LINUX)
    # Laptop.objects.filter(brand__in=(
    #     LaptopBrandChoice.DELL, LaptopBrandChoice.ACER
    # )).update(operation_system=OperationSystemChoice.LINUX)
    # # Laptop.objects.filter(brand="Lenovo").update(operation_system=OperationSystemChoice.CHROME_OS)
    # Laptop.objects.filter(brand=LaptopBrandChoice.LENOVO).update(operation_system=OperationSystemChoice.CHROME_OS)

    Laptop.objects.update(operation_system=Case(
        When(brand=LaptopBrandChoice.ASUS, then=Value(OperationSystemChoice.WINDOWS)),
        When(brand=LaptopBrandChoice.APPLE, then=Value(OperationSystemChoice.MACOS)),
        When(brand__in=(LaptopBrandChoice.DELL, LaptopBrandChoice.ACER), then=Value(OperationSystemChoice.LINUX)),
        When(brand=LaptopBrandChoice.LENOVO, then=Value(OperationSystemChoice.CHROME_OS)),
    ))


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player() -> None:
    # ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")
    ChessPlayer.objects.filter(rating__lte=2199).update(title="regular player")


def set_new_chefs() -> None:
    Meal.objects.update(chef=Case(
        When(meal_type=MealTypeChoices.BREAKFAST, then=Value("Gordon Ramsay")),
        When(meal_type=MealTypeChoices.LUNCH, then=Value("Julia Child")),
        When(meal_type=MealTypeChoices.DINNER, then=Value("Jamie Oliver")),
        When(meal_type=MealTypeChoices.SNACK, then=Value("Thomas Keller")),
    ))


def set_new_preparation_times() -> None:
    Meal.objects.update(preparation_time=Case(
        When(meal_type=MealTypeChoices.BREAKFAST, then=Value("10 minutes")),
        When(meal_type=MealTypeChoices.LUNCH, then=Value("12 minutes")),
        When(meal_type=MealTypeChoices.DINNER, then=Value("15 minutes")),
        When(meal_type=MealTypeChoices.SNACK, then=Value("5 minutes")),
    ))


def update_low_calorie_meals() -> None:
    # Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)
    Meal.objects.filter(
        meal_type__in=(MealTypeChoices.BREAKFAST, MealTypeChoices.DINNER)
    ).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(
        meal_type__in=(MealTypeChoices.LUNCH, MealTypeChoices.SNACK)
    ).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(
        meal_type__in=(MealTypeChoices.LUNCH, MealTypeChoices.SNACK)
    ).delete()


def show_hard_dungeons() -> str or None:
    hard_dungeons = Dungeon.objects.filter(difficulty=DifficultyChoices.HARD).order_by('-location')

    return '\n'.join(f"{hd.name} is guarded by {hd.boss_name} who has {hd.boss_health} health points!" for hd in hard_dungeons)


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names() -> None:
    Dungeon.objects.filter(difficulty=DifficultyChoices.EASY).update(name="The Erased Thombs")
    Dungeon.objects.filter(difficulty=DifficultyChoices.MEDIUM).update(name="The Coral Labyrinth")
    Dungeon.objects.filter(difficulty=DifficultyChoices.HARD).update(name="The Lost Haunt")


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(recommended_level=Case(
        When(difficulty=DifficultyChoices.EASY, then=Value(25)),
        When(difficulty=DifficultyChoices.MEDIUM, then=Value(50)),
        When(difficulty=DifficultyChoices.HARD, then=Value(75)),
    ))


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations() -> None:
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


def show_workouts() -> str or None:
    workouts = Workout.objects.filter(
        workout_type__in=(WorkoutTypeChoices.CALISTHENICS, WorkoutTypeChoices.CROSSFIT)
    ).order_by('id')

    return '\n'.join(f"{w.name} from {w.workout_type} type has {w.difficulty} difficulty!" for w in workouts)


def get_high_difficulty_cardio_workouts() -> QuerySet or None:
    return Workout.objects.filter(workout_type="Cardio", difficulty="High").order_by('instructor')


def set_new_instructors() -> None:
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CARDIO).update(instructor="John Smith")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.STRENGTH).update(instructor="Michael Williams")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.YOGA).update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CROSSFIT).update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type=WorkoutTypeChoices.CALISTHENICS).update(instructor="Chris Heria")


def set_new_duration_times() -> None:
    Workout.objects.update(duration=Case(
        When(instructor="John Smith", then=Value("15 minutes")),
        When(instructor="Sarah Davis", then=Value("30 minutes")),
        When(instructor="Chris Heria", then=Value("45 minutes")),
        When(instructor="Michael Williams", then=Value("1 hour")),
        When(instructor="Emily Johnson", then=Value("1 hour and 30 minutes")),
    ))


def delete_workouts() -> None:
    Workout.objects.exclude(
        workout_type__in=(WorkoutTypeChoices.STRENGTH, WorkoutTypeChoices.CALISTHENICS)
    ).delete()
