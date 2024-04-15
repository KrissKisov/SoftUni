from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):

    def setUp(self):
        self.shop = PetShop("Pet Shop")

    def test_correct_init(self):
        self.assertEqual("Pet Shop", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_with_invalid_quantity_of_food_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("dog food", 0)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_expect_success(self):
        self.shop.food = {"dog food": 20}

        result_1 = self.shop.add_food("cat food", 100)
        expected_1 = f"Successfully added 100.00 grams of cat food."

        self.assertEqual({"dog food": 20, "cat food": 100}, self.shop.food)
        self.assertEqual(expected_1, result_1)

        result_2 = self.shop.add_food("dog food", 80)
        expected_2 = "Successfully added 80.00 grams of dog food."

        self.assertEqual({"dog food": 100, "cat food": 100}, self.shop.food)
        self.assertEqual(expected_2, result_2)

    def test_add_pet_with_name_already_in_collection_raises_error(self):
        self.shop.pets = ["dog", "cat"]

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("dog")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_expect_success(self):
        self.shop.pets = ["dog", "cat"]

        expected = "Successfully added parrot."
        result = self.shop.add_pet("parrot")

        self.assertEqual(["dog", "cat", "parrot"], self.shop.pets)
        self.assertEqual(expected, result)

    def test_feed_pet_with_invalid_pet_name_raises_error(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"dog food": 100, "cat food": 100, "seeds": 100}

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("seeds", "parrot")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_non_existing_food_returns_appropriate_message(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"cat food": 100, "seeds": 100}

        expected = "You do not have dog food"
        result = self.shop.feed_pet("dog food", "dog")

        self.assertEqual(expected, result)

    def test_feed_pet_with_not_enough_food_returns_appropriate_message(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"dog food": 99, "cat food": 100}

        expected = "Adding food..."
        result = self.shop.feed_pet("dog food", "dog")

        self.assertEqual({"dog food": 1099, "cat food": 100}, self.shop.food)
        self.assertEqual(expected, result)

    def test_feed_pet_expect_success(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"dog food": 100, "cat food": 200}

        expected_1 = "cat was successfully fed"
        result_1 = self.shop.feed_pet("cat food", "cat")

        self.assertEqual({"dog food": 100, "cat food": 100}, self.shop.food)
        self.assertEqual(expected_1, result_1)

        expected_2 = "dog was successfully fed"
        result_2 = self.shop.feed_pet("dog food", "dog")

        self.assertEqual({"dog food": 0, "cat food": 100}, self.shop.food)
        self.assertEqual(expected_2, result_2)

    def test__repr__(self):
        self.shop.pets = ["dog", "cat"]

        self.assertEqual("Shop Pet Shop:\nPets: dog, cat", self.shop.__repr__())


if __name__ == "__main__":
    main()
