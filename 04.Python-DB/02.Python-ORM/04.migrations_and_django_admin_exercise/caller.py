import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Supplier, Course, Person, SmartPhone


# Create queries within functions

def add_person():

    # Adding 1st person
    person_1 = Person(
        name='John Doe',
        age=23
    )
    person_1.save()

    # Adding 2nd person
    person_2 = Person(
        name='Jane Boye',
        age=34
    )
    person_2.save()

    # Adding 3rd person
    person_3 = Person(
        name='Phill Page',
        age=28
    )
    person_3.save()


def add_course():

    # Adding 1st course
    course_1 = Course(
        title='PythonSQL',
        lecturer='Dian',
        description='Some description about the course',
        price=310.00,
    )
    course_1.save()

    # Adding 2nd course
    course_2 = Course(
        title='PythonOOP',
        lecturer='Ines',
        description='Course about object-oriented programming',
        price=290.00,
    )
    course_2.save()

    return 'Successfully added 2 courses'


def create_supplier():

    # Adding first supplier
    supplier_1 = Supplier(
        name='Coca-Cola',
        contact_person='Ivan',
        email='Ivan@Coca-Cola.com',
        phone='09999911111333',
        address='Plovdiv, Bulgaria',
    )
    supplier_1.save()

    # Adding second supplier
    supplier_2 = Supplier(
        name='Pepsi',
        contact_person='Peter',
        email='Peter@Pepsi.com',
        phone='08856573368393',
        address='Sofia, Bulgaria'
    )
    supplier_2.save()

    return 'Successfully created 2 supplier'


def add_smartphone() -> str:
    smart_phone_1 = SmartPhone(
        brand='Huawei',
        price=459.99,
        category="No category",
    )
    smart_phone_1.save()

    smart_phone_2 = SmartPhone(
        brand='Samsung',
        price=559.99,
        category="No category",
    )
    smart_phone_2.save()

    smart_phone_3 = SmartPhone(
        brand='Apple',
        price=759.99,
        category="No category",
    )
    smart_phone_3.save()

    return 'Successfully added 3 smartphones'


# print(create_supplier())

# print(add_course())

# print(add_person())

# print(add_smartphone())