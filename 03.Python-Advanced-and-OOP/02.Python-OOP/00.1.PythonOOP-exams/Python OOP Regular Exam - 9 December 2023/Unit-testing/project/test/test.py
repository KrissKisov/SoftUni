from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.s = RailwayStation("Oxford")

    def test_correct_init(self):
        self.assertEqual("Oxford", self.s.name)
        self.assertEqual(deque(), self.s.arrival_trains)
        self.assertEqual(deque(), self.s.departure_trains)

    def test_name_setter_invalid_length_name_raises_error(self):
        expected = "Name should be more than 3 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.s.name = "Oxf"

        self.assertEqual(expected, str(ve.exception))

    def test_new_train_arrive_expect_success(self):
        self.s.new_arrival_on_board("New train")

        self.assertEqual(self.s.arrival_trains, deque(["New train"]))
        self.assertEqual(len(self.s.arrival_trains), 1)

    def test_train_has_arrived_with_other_trains_before_that(self):
        self.s.new_arrival_on_board("First train")

        expected = "There are other trains to arrive before Second train."
        result = self.s.train_has_arrived("Second train")

        self.assertEqual(expected, result)

    def test_train_has_arrived_with_no_other_trains_before_that(self):
        self.s.new_arrival_on_board("First train")

        expected = "First train is on the platform and will leave in 5 minutes."
        result = self.s.train_has_arrived("First train")

        self.assertEqual(expected, result)
        self.assertEqual(self.s.departure_trains, deque(["First train"]))

    def test_train_has_left_with_no_departure_train(self):

        result = self.s.train_has_left("Some train")

        self.assertFalse(result)

    def test_train_has_left_with_other_train_before_that(self):
        self.s.departure_trains = deque(["First train", "Some train"])

        result = self.s.train_has_left("Some train")

        self.assertFalse(result)

    def test_train_has_left_with_correct_train(self):
        self.s.departure_trains = deque(["First train"])

        result = self.s.train_has_left("First train")

        self.assertTrue(result)


if __name__ == "__main__":
    main()
