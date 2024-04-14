from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team("Test")
        self.other = Team("Other")

    def test_correct_init(self):
        self.assertEqual("Test", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_with_invalid_symbol_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "test12"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_expect_success(self):
        expected = f"Successfully added: Ivan, Peter"
        result = self.team.add_member(Ivan=30, Peter=35)

        self.assertEqual({"Ivan": 30, "Peter": 35}, self.team.members)
        self.assertEqual(expected, result)

    def test_add_member_with_existing_names_adds_only_new_names(self):
        self.team.members = {"Ivan": 30, "Peter": 35}

        expected = f"Successfully added: Kriss, Nora"
        result = self.team.add_member(Ivan=30, Peter=35, Kriss=40, Nora=36)

        self.assertEqual({"Ivan": 30, "Peter": 35, "Kriss": 40, "Nora": 36}, self.team.members)
        self.assertEqual(expected, result)

    def test_remove_member_expect_success(self):
        self.team.members = {"Ivan": 30, "Peter": 35, "Kriss": 40, "Nora": 36}

        expected = f"Member Peter removed"
        result = self.team.remove_member("Peter")

        self.assertEqual({"Ivan": 30, "Kriss": 40, "Nora": 36}, self.team.members)
        self.assertEqual(expected, result)

    def test_remove_non_existing_member_return_correct_message(self):
        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}

        expected = f"Member with name Ivan does not exist"
        result = self.team.remove_member("Ivan")

        self.assertEqual({"Peter": 35, "Kriss": 40, "Nora": 36}, self.team.members)
        self.assertEqual(expected, result)

    def test__len__(self):
        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}

        self.assertEqual(3, self.team.__len__())

    def test__gt__expect_true(self):
        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}
        self.other.members = {"Kriss": 40, "Nora": 36}
        # self.assertTrue(self.team.__gt__(self.other))  # 'assertTrue() does not work in judge
        self.assertEqual(True, self.team.__gt__(self.other))

    def test__gt__expect_false(self):

        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}
        self.other.members = {"Ivan": 30, "Peter": 35, "Kriss": 40, "Nora": 36}
        self.assertFalse(self.team.__gt__(self.other))

        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}
        self.other.members = {"Ivan": 30, "Peter": 35, "Kriss": 40}
        self.assertFalse(self.team.__gt__(self.other))

    def test__add__expect_success(self):
        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36}
        self.other.members = {"Ivan": 30, "Peter": 35, "Kriss": 40}

        expected = f"{self.team.name}{self.other.name}"
        self.new_team = self.team.__add__(self.other)

        self.assertEqual({"Peter": 35, "Kriss": 40, "Nora": 36, "Ivan": 30}, self.new_team.members)
        self.assertEqual(expected, self.new_team.name)

    def test__str__(self):
        self.team.members = {"Peter": 35, "Kriss": 40, "Nora": 36, "Ivan": 35}
        expected = (f"Team name: {self.team.name}\n"
                    f"Member: Kriss - 40-years old\n"
                    f"Member: Nora - 36-years old\n"
                    f"Member: Ivan - 35-years old\n"
                    f"Member: Peter - 35-years old")

        result = self.team.__str__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
