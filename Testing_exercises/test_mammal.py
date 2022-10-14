

import unittest

class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal(name='Test', mammal_type='Dog', sound='Woof')

    def test_if_constructor_is_initiliazied_correctly(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('Dog', self.mammal.type)
        self.assertEqual('Woof', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_if_sound_is_correct(self):
        actual = self.mammal.make_sound()
        expected = 'Test makes Woof'
        self.assertEqual(expected, actual)

    def test_if_kindgom_is_correct(self):
        rest = self.mammal.get_kingdom()
        self.assertEqual('animals', rest)

    def test_if_get_info_is_correct(self):

        actual = self.mammal.info()
        expected = 'Test is of type Dog'

        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()