class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.added_students = 0

    def add_student(self, name: str, grade: float):
        if Class.__students_count > self.added_students:
            self.students.append(name)
            self.grades.append(grade)
            self.added_students += 1

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self):.2f}"


# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)
