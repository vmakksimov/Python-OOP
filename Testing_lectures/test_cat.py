from Testing.cat import Cat

import unittest

class CatTests(unittest.TestCase):

    def test_if_is_initialized_correctly(self):
        cat = Cat('Test')
        self.assertEqual('Test', cat.name)
        self.assertFalse(cat.sleepy)
        self.assertFalse(cat.fed)
        self.assertEqual(0, cat.size)


    def test_if_cats_size_increased_after_eating(self):
        cat = Cat('Test')
        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)


    def test_if_cats_fed_after_eating(self):
        cat = Cat('Test')
        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_if_cats_fed(self):
        cat = Cat('Test')
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()

            # assertion
        self.assertEqual('Already fed.', str(ex.exception))


    def test_if_cats_sleep(self):
        cat = Cat('Test')
        self.assertFalse(cat.fed)



        with self.assertRaises(Exception) as ex:
            cat.sleep()

            # assertion
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


    def test_is_not_sleepy(self):
        cat = Cat('Test')
        self.assertFalse(cat.sleepy)
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()

