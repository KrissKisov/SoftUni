import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


def add_students() -> None:
    student = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )
    student.save()

    student = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com',
    )
    student.save()

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


def get_students_info() -> str:
    output = []
    students = Student.objects.all()

    for student in students:
        output.append(f'Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}')

    return '\n'.join(output)


def update_students_emails() -> None:
    students = Student.objects.all()

    for student in students:
        student.email = student.email.replace(student.email.split('@')[1], 'uni-students.com')
        student.save()


def truncate_students() -> None:
    students = Student.objects.all().delete()


# Run and print your queries

# add_students()
# print(Student.objects.all())

# print(get_students_info())

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
