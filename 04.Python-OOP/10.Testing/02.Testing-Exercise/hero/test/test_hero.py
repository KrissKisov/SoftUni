from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_raises_exception_when_try_to_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_zero_health_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_when_enemy_health_is_zero_raises_value_error(self):
        self.enemy.health = 0
        expected_output = "You cannot fight Enemy. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_output, str(ve.exception))

    def test_battle_with_draw_result_returns_draw_and_decreases_health_on_both_players(self):
        self.enemy.damage = 100

        expected_output = self.hero.battle(self.enemy)

        self.assertEqual("Draw", expected_output)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_when_hero_win_returns_correct_string_and_increases_his_stats(self):
        expected = self.hero.battle(self.enemy)

        self.assertEqual("You win", expected)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_when_enemy_win_returns_correct_string_and_increases_his_stats(self):
        self.enemy.health = 150
        self.enemy.damage = 150

        expected = self.hero.battle(self.enemy)

        self.assertEqual("You lose", expected)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(155, self.enemy.damage)

    def test_str_method_returns_correct_string(self):
        self.assertEqual(
            "Hero Hero: 1 lvl\n"
            "Health: 100\n"
            "Damage: 100\n",
            self.hero.__str__()
        )


if __name__ == "__main__":
    main()
