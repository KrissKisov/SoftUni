from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_without_courses = Student("Student_1", None)
        self.student_with_courses = Student("Student_2", {"python": ["print('Hi')"]})

    def test_correct_init(self):
        self.assertEqual("Student_1", self.student_without_courses.name)
        self.assertEqual("Student_2", self.student_with_courses.name)

        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual({"python": ["print('Hi')"]}, self.student_with_courses.courses)

    def test_enroll_to_the_same_course_appends_new_notes(self):
        result = self.student_with_courses.enroll(
            "python",
            ["class Hero", "class TestHero"]
        )

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(
            ["print('Hi')", "class Hero", "class TestHero"],
            self.student_with_courses.courses["python"]
        )

    def test_enroll_to_new_course_without_third_parameter_adds_the_notes(self):
        result = self.student_without_courses.enroll("python", ["def some_func", "return result"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(
            {"python": ["def some_func", "return result"]},
            self.student_without_courses.courses
        )

    def test_enroll_to_new_course_with_third_parameter_Y_adds_the_notes(self):
        result = self.student_without_courses.enroll(
            "python",
            ["def some_func", "return result"],
            "Y"
        )

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(
            {"python": ["def some_func", "return result"]},
            self.student_without_courses.courses
        )

    def test_enroll_to_new_course_with_third_parameter_N_does_not_add_the_notes(self):
        result = self.student_without_courses.enroll(
            "python",
            ["def some_func", "return result"],
            "N"
        )

        self.assertEqual("Course has been added.", result)
        self.assertEqual(
            {"python": []},
            self.student_without_courses.courses
        )

    def test_add_notes_to_enrolled_course_expect_success(self):
        result = self.student_with_courses.add_notes("python", "def some_new_func")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["print('Hi')", "def some_new_func"], self.student_with_courses.courses["python"])

    def test_add_notes_to_not_enrolled_course_raises_exception(self):
        expected = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student_without_courses.add_notes("python", "print('Say Hi')")

        self.assertEqual(expected, str(ex.exception))

    def test_leave_enrolled_course(self):
        expected = "Course has been removed"
        result = self.student_with_courses.leave_course("python")

        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual(expected, result)

    def test_leave_not_enrolled_course_raises_exception(self):
        expected = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student_without_courses.leave_course("python")

        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()
