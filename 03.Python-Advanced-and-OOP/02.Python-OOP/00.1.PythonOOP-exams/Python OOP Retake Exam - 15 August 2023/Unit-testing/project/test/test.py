from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {
        'New Zealand': 7500,
        'Australia': 5700,
        'Brazil': 6200,
        'Bulgaria': 500,
    }

    def setUp(self):
        self.trip1 = Trip(10_000, 2, True)
        self.trip2 = Trip(10_000, 2, False)

    def test_correct_init(self):
        self.assertEqual(10_000, self.trip1.budget)
        self.assertEqual(2, self.trip1.travelers)
        self.assertTrue(self.trip1.is_family)
        self.assertEqual({}, self.trip1.booked_destinations_paid_amounts)

    def test_traveler_setter_with_invalid_number_raises_error(self):
        expected = "At least one traveler is required!"

        with self.assertRaises(ValueError) as ve:
            self.trip1.travelers = 0

        self.assertEqual(expected, str(ve.exception))

    def test_family_setter_with_less_travelers_returns_false(self):
        self.trip1.travelers = 1
        self.trip1.is_family = True

        self.assertEqual(False, self.trip1.is_family)

    def test_family_setter_with_enough_people_but_not_family_returns_false_for_is_family(self):
        self.assertEqual(False, self.trip2.is_family)
        self.assertFalse(self.trip2.is_family)

    def test_family_setter_returns_true(self):
        self.assertTrue(self.trip1.is_family)

    def test_book_a_trip_with_invalid_destination_return_error_message(self):
        expected = "This destination is not in our offers, please choose a new one!"
        result = self.trip1.book_a_trip("Italy")

        self.assertEqual(expected, result)

    def test_book_a_trip_with_valid_destination_and_enough_budget(self):
        expected1 = "Successfully booked destination Bulgaria! Your budget left is 9100.00"
        expected2 = "Successfully booked destination Bulgaria! Your budget left is 9000.00"

        result1 = self.trip1.book_a_trip("Bulgaria")
        result2 = self.trip2.book_a_trip("Bulgaria")

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

        self.assertEqual(9100.00, self.trip1.budget)
        self.assertEqual(9000.00, self.trip2.budget)

        self.assertEqual({"Bulgaria": 900}, self.trip1.booked_destinations_paid_amounts)
        self.assertEqual({"Bulgaria": 1000}, self.trip2.booked_destinations_paid_amounts)

    def test_book_a_trip_with_valid_destination_and_not_enough_budget(self):
        expected1 = "Your budget is not enough!"
        expected2 = "Your budget is not enough!"

        result1 = self.trip1.book_a_trip("New Zealand")
        result2 = self.trip2.book_a_trip("New Zealand")

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

        self.assertEqual(10000.00, self.trip1.budget)
        self.assertEqual(10000.00, self.trip2.budget)

        self.assertEqual({}, self.trip1.booked_destinations_paid_amounts)
        self.assertEqual({}, self.trip2.booked_destinations_paid_amounts)

    def test_booking_status_without_bookings(self):
        self.assertEqual("No bookings yet. Budget: 10000.00", self.trip2.booking_status())

    def test_booking_status_with_bookings(self):
        self.trip1.budget = 30_000

        self.trip1.book_a_trip("Bulgaria")
        self.trip1.book_a_trip("New Zealand")

        expected = ("Booked Destination: Bulgaria\n"
                    "Paid Amount: 900.00\n"
                    "Booked Destination: New Zealand\n"
                    "Paid Amount: 13500.00\n"
                    "Number of Travelers: 2\n"
                    "Budget Left: 15600.00")
        self.assertEqual(expected, self.trip1.booking_status())

if __name__ == "__main__":
    main()
