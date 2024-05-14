from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.int_list = IntegerList(3.49, 1, 2, 3, 4, "hi")

    def test_correct_initialization_ignoring_non_int_values(self):
        self.assertEqual([1, 2, 3, 4], self.int_list.get_data())

    def test_raise_value_error_when_non_int_element_added_to_list(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add(2.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_adding_element_to_the_list_when_element_is_integer(self):
        # expected_output = [1, 2, 3, 4, 5]
        expected_output = self.int_list.get_data() + [5]

        self.int_list.add(5)

        self.assertEqual(expected_output, self.int_list.get_data())

    def test_raise_index_error_when_removing_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_when_the_index_is_valid(self):
        expected_output = [1, 2, 3]

        self.int_list.remove_index(3)

        self.assertEqual(expected_output, self.int_list.get_data())

    def test_raise_index_error_when_get_method_is_called_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(17)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_when_called_with_valid_index(self):
        expected_output = self.int_list.get(2)

        self.assertEqual(3, expected_output)

    def test_raise_index_error_when_insert_method_is_called_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(6, 24)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_raise_value_error_when_insert_method_is_called_with_valid_index_but_non_int_element(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(2, 3.45)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_with_valid_index_and_int_element(self):
        # expected = [1, 2, 17, 3, 4]
        expected = self.int_list.get_data().copy()
        expected.insert(2, 17)

        self.int_list.insert(2, 17)

        self.assertEqual(expected, self.int_list.get_data())

    def test_method_get_biggest(self):
        expected = self.int_list.get_biggest()

        self.assertEqual(4, expected)

    def test_method_get_index(self):
        expected = self.int_list.get_index(4)

        self.assertEqual(3, expected)


if __name__ == "__main__":
    main()
