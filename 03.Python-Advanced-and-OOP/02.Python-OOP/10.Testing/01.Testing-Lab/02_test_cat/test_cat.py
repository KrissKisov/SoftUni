from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Macharok")

    def test_class_initializes_correctly(self):
        self.assertEqual("Macharok", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_size_is_increased_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_and_sleepy_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_raise_exception_error_if_cat_eat_when_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_raise_exception_error_when_method_sleep_is_called_but_cat_is_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_not_sleepy_after_sleep_method_is_called(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
