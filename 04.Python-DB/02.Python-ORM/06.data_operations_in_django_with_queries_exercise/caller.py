import os
from datetime import datetime, timedelta
import django
from django.db.models import QuerySet, F


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str) -> str:
    # pet = Pet.objects.create(name=name, species=species)
    pet = Pet(name=name, species=species)
    pet.save()

    return f'{pet.name} is a very cute {pet.species}!'


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f'The artifact {artifact.name} is {artifact.age} years old!'


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def create_location(name: str, region: str, population: int, description: str, is_capital: bool) -> None:
    Location.objects.create(
        name=name,
        region=region,
        population=population,
        description=description,
        is_capital=is_capital
    )


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')
    locations_output = []
    for location in locations:
        locations_output.append(f'{location.name} has a population of {location.population}!')

    return '\n'.join(locations_output)


def new_capital() -> None:
    capital = Location.objects.first()
    capital.is_capital = True
    capital.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def create_car(model: str, year: int, color: str, price: float) -> None:
    Car.objects.create(
        model=model,
        year=year,
        color=color,
        price=price
    )


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        per_cent_of_discount = sum(int(x) for x in str(car.year))
        car.price_with_discount = car.price * (100 - per_cent_of_discount) / 100
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def add_task() -> None:
    task = (
        Task(
            title='First task',
            description='This is the first task description',
            due_date=datetime.today() + timedelta(days=10),
            is_finished=False,
        ),
        Task(
            title='Second task',
            description='This is the second task description',
            due_date=datetime.today() + timedelta(days=13),
            is_finished=False,
        ),
        Task(
            title='Third task',
            description='This is the third task description',
            due_date=datetime.today() + timedelta(days=17),
            is_finished=False,
        ),
        Task(
            title='Fourth task',
            description='This is the fourth task description',
            due_date=datetime.today() + timedelta(days=20),
            is_finished=False,
        ),
    )
    Task.objects.bulk_create(task)


def show_unfinished_tasks() -> str:
    tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(f"Task - {t.title} needs to be done until {t.due_date}!" for t in tasks)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(s) - 3) for s in text)

    Task.objects.filter(title=task_title).update(description=decoded_text)


def add_hotel_room() -> None:
    HotelRoom.objects.create(
        room_number=401,
        room_type='Standard',
        capacity=2,
        amenities='Tv',
        price_per_night=100.00
    )
    HotelRoom.objects.create(
        room_number=501,
        room_type='Deluxe',
        capacity=3,
        amenities='Wi-Fi',
        price_per_night=200.00
    )
    HotelRoom.objects.create(
        room_number=601,
        room_type='Deluxe',
        capacity=6,
        amenities='Jacuzzi',
        price_per_night=400.00
    )


def get_deluxe_rooms() -> str or None:
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')

    if deluxe_rooms:
        return '\n'.join(f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!" for r
                         in deluxe_rooms if r.id % 2 == 0)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if room.is_reserved:
            if previous_room_capacity is None:
                room.capacity += room.id
            else:
                room.capacity += previous_room_capacity

            previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=('Assassin', 'Scout')).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    name = f"{first_character.name} {second_character.name}"
    class_name = "Fusion"
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = (first_character.hit_points + second_character.hit_points)
    if first_character.class_name in ('Mage', 'Scout'):
        inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    else:
        inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory='The inventory is empty').delete()


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)
# # delete_all_artifacts()

# create_location('Sofia',	'Sofia Region',	1329000,	'The capital of Bulgaria and the largest city in the country',	False)
# create_location('Plovdiv',	'Plovdiv Region',	346942,	'The second-largest city in Bulgaria with a rich historical heritage',	False)
# create_location('Varna', 'Varna Region',	330486,	'A city known for its sea breeze and beautiful beaches on the Black Sea',	False)
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
# delete_first_location()

# create_car('Mercedes C63 AMG',	2019,	'white',	120000.00)
# create_car('Audi Q7 S line',	2023,	'black',	183900.00)
# create_car('Chevrolet Corvette',	2021,	'dark grey',	199999.00)

# apply_discount()
# print(get_recent_cars())
## Car.objects.all().delete()

# add_task()
# print(show_unfinished_tasks())
# complete_odd_tasks()
# encode_and_replace('abcd', 'First task')

# add_hotel_room()
# print(get_deluxe_rooms())
# increase_room_capacity()
# reserve_first_room()

# update_characters()
# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
