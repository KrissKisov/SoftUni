from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):

    def setUp(self):
        self.src = StudentReportCard("Some_Student", 8)
        self.src2 = StudentReportCard("Some_Student", 8)

    def test_correct_init(self):
        self.assertEqual("Some_Student", self.src.student_name)
        self.assertEqual(8, self.src.school_year)
        self.assertEqual({}, self.src.grades_by_subject)

    def test_student_name_setter_with_empty_string_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.src.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_setter_with_invalid_value_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.src.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.src.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_setter_expect_success(self):
        self.src.school_year = 12
        self.assertEqual(12, self.src.school_year)

        self.src2.school_year = 1
        self.assertEqual(1, self.src2.school_year)

    def test_add_grade_expect_success(self):
        self.src.grades_by_subject = {"Python": [5.90]}
        self.src.add_grade("Python", 6.00)
        self.src.add_grade("Java", 6.00)
        expected = {"Python": [5.90, 6.00], "Java": [6.00]}
        self.assertEqual(expected, self.src.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.src.grades_by_subject = {"Python": [5.90, 6.00], "Java": [6.00]}
        expected = ('Python: 5.95\n'
                    'Java: 6.00')

        result = self.src.average_grade_by_subject()

        self.assertEqual(expected, result)

        self.src2.grades_by_subject = {}
        self.assertEqual("", self.src2.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.src.grades_by_subject = {"Python": [5.90, 6.00], "Java": [6.00]}

        expected = f"Average Grade: 5.97"

        result = self.src.average_grade_for_all_subjects()

        self.assertEqual(expected, result)

    def test_repr_method(self):
        self.src.grades_by_subject = {"Python": [5.90, 6.00], "Java": [6.00]}

        expected = f"Name: {self.src.student_name}\n" \
                   f"Year: {self.src.school_year}\n" \
                   f"----------\n" \
                   f"{self.src.average_grade_by_subject()}\n" \
                   f"----------\n" \
                   f"{self.src.average_grade_for_all_subjects()}"

        result = self.src.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
