from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("name", "type", "sound")

    def test_correct_init(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        # self.assertEqual("animals", self.mammal._Mammal__kingdom)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_method_make_sound_returns_correct_string(self):
        self.assertEqual("name makes sound", self.mammal.make_sound())

    def test_info_method_returns_correct_string(self):
        self.assertEqual("name is of type type", self.mammal.info())


if __name__ == "__main__":
    main()
