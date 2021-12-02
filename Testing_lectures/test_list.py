from Testing.list_value import IntegerList

import unittest

class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.list_int = IntegerList(5, 6, 7)

    def test_if_is_initialized_correctly(self):
        #testvane na private atribut
        self.assertEqual([5,6,7], self.list_int._IntegerList__data)

    def test_check_if_number_is_not_integer(self):
        list_int = IntegerList(4.5, '6', 7.2)
        self.assertEqual([], list_int._IntegerList__data)

    def add_element_to_the_list(self):
        result = self.list_int.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def add_element_not_integer(self):
        result = self.list_int.add(5.5)
        with self.assertRaises(ValueError) as ex:
            self.list_int.add(result)

        #assertion
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        self.list_int.remove_index(0)
        self.assertEqual([6, 7], self.list_int._IntegerList__data)

    def test_if_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_int.remove_index(3)

        # assertion
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_get_element(self):
        self.list_int.get(0)
        self.assertEqual([5, 6, 7], self.list_int._IntegerList__data)

    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_int.get(3)

        # assertion
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element(self):
        self.list_int.insert(0, 10)
        self.assertEqual([10, 5, 6, 7], self.list_int._IntegerList__data)


    def test_if_index_out_of_range_insert(self):
        with self.assertRaises(IndexError) as ex:
            self.list_int.insert(3, 10)

        # assertion
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_el_not_an_integer_insert(self):
        with self.assertRaises(ValueError) as ex:
            self.list_int.insert(0, 5.5)

        #assertion
        self.assertEqual("Element is not Integer", str(ex.exception))


    def test_get_biggest(self):
        result = self.list_int.get_biggest()
        self.assertEqual(7, result)

    def test_get_index(self):
        result = self.list_int.get_index(5)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
