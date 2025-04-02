from unittest import TestCase, main
from Inheritance.players_and_monsters.project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("test", 5, 10, 2)
        self.enemy = Hero("enemy", 6, 12, 3)

    def test_correct_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_try_to_fight_yourself_throws_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_fight_with_health_equal_to_zero_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_health_lower_than_zero_raises_value_error(self):
        self.hero.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_enemy_with_health_lower_than_zero_raises_value_error(self):
        self.enemy.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_draw_between_players_returns_draw(self):
        self.hero = Hero("test", 2, 10, 5)
        self.enemy = Hero("enemy", 6, 10, 2)

        returned_result = self.hero.battle(self.enemy) #"Draw"
        self.assertEqual("Draw", returned_result)
        self.assertEqual(-2, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_hero_wins_and_only_enemy_health_goes_to_zero_returns_string_you_win(self):
        self.hero = Hero("test", 2, 10, 5)
        self.enemy = Hero("enemy", 4, 10, 2)

        returned_result = self.hero.battle(self.enemy)
        self.assertEqual("You win", returned_result)
        self.assertEqual(7, self.hero.health)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(0, self.enemy.health)

    def test_enemy_wins_heros_health_goes_down_enemy_upgrades_and_you_lose_string_is_returned(self):
        self.enemy = Hero("test", 2, 10, 5)
        self.hero = Hero("enemy", 4, 10, 2)

        returned_result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", returned_result)
        self.assertEqual(7, self.enemy.health)
        self.assertEqual(3, self.enemy.level)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual(0, self.hero.health)

    def test_that_printing_hero_returns_the_correct_string(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n", f"{self.hero}")











if __name__ == "__main__":
    main()