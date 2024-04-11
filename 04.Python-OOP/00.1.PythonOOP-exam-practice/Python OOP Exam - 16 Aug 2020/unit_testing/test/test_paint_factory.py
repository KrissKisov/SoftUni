from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self):
        self.pf = PaintFactory("Test", 100)

    def test_correct_init(self):
        self.assertEqual("Test", self.pf.name)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)
        self.assertEqual({}, self.pf.products)
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_with_invalid_product_type_raises_error(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("black", 10)

        expected = f"Ingredient of type black not allowed in {self.pf.__class__.__name__}"

        self.assertEqual(expected, str(te.exception))

    def test_add_ingredient_with_invalid_product_quantity_raises_error(self):
        self.pf.ingredients = {"white": 30, "yellow": 30, "green": 20, "red": 20}

        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("blue", 10)

        expected = "Not enough space in factory"

        self.assertEqual(expected, str(ve.exception))

    def test_add_ingredient_expect_success(self):
        self.pf.ingredients = {"white": 20, "yellow": 20, "green": 20, "red": 20}

        expected = {"white": 20, "yellow": 20, "green": 20, "red": 20, "blue": 10}
        self.pf.add_ingredient("blue", 10)
        self.assertEqual(expected, self.pf.ingredients)

        expected = {"white": 30, "yellow": 20, "green": 20, "red": 20, "blue": 10}
        self.pf.add_ingredient("white", 10)
        self.assertEqual(expected, self.pf.ingredients)

    def test_remove_ingredient_with_invalid_ingredient_raises_error(self):
        self.pf.ingredients = {"white": 20, "yellow": 20, "green": 20, "red": 20}

        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("blue", 20)

        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_with_invalid_quantity_raises_error(self):
        self.pf.ingredients = {"white": 20, "yellow": 20, "green": 20, "red": 20}

        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 21)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_expect_success(self):
        self.pf.ingredients = {"white": 20, "yellow": 20, "green": 20, "red": 20}

        expected = {"white": 10, "yellow": 20, "green": 20, "red": 20}
        self.pf.remove_ingredient("white", 10)

        self.assertEqual(expected, self.pf.ingredients)

    def test_product(self):
        self.pf.ingredients = {"white": 20, "yellow": 20, "green": 20, "red": 20}

        self.assertEqual(self.pf.ingredients, self.pf.products)


if __name__ == "__main__":
    main()
