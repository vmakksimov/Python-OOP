from project.hero import Hero

import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(username='Viktor', level=100, health=90.5, damage=95.5)
        self.enemy = Hero(username='Lorenzo', level=50, health=50.5, damage=40.5)

    def test_check_if_init_is_correct(self):
        self.assertEqual('Viktor', self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(90.5, self.hero.health)
        self.assertEqual(95.5, self.hero.damage)

    def test_check_if_battle_is_possible(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_check_if_health_is_enough(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_check_if_health_enemy_is_enough(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Lorenzo. He needs to rest", str(ex.exception))

    def test_check_if_draw(self):
        self.enemy.health = 20
        self.hero.health = 20
        res = self.hero.battle(self.enemy)
        self.assertEqual('Draw', res)

    def test_check_if_you_win(self):
        self.hero.health = 2026
        res_f = self.hero.battle(self.enemy)
        self.assertEqual(101, self.hero.level)
        self.assertEqual(6, self.hero.health)
        self.assertEqual(100.5, self.hero.damage)
        self.assertEqual('You win', res_f)

    def test_check_if_you_lose(self):
        self.enemy.health = 9551
        res_f = self.hero.battle(self.enemy)
        self.assertEqual(51, self.enemy.level)
        self.assertEqual(6, self.enemy.health)
        self.assertEqual(45.5, self.enemy.damage)
        self.assertEqual('You lose', res_f)

    def test_check_str(self):
        actual = self.hero.__str__()
        expected = "Hero Viktor: 100 lvl\n" \
                   "Health: 90.5\n" \
                   "Damage: 95.5\n"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
