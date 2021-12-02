from Testing.car_manager import Car

import unittest

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(make='E92', model='BMW', fuel_consumption=10, fuel_capacity=60)

    def test_is_initialiazied(self):

        self.assertEqual('E92',  self.car.make)
        self.assertEqual('BMW', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_is_make_not_empty(self):
        self.car.make = 'E92'
        self.assertEqual('E92', self.car.make)

    def test_is_make_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

            # assertion
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_is_model_not_empty(self):
        self.car.model = 'BMW'
        self.assertEqual('BMW', self.car.model)

    def test_is_model_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

            # assertion
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))


    def test_car_fuel_consumption_used(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_car_check_if_fuel_consumption_is_zer_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5

            # assertion
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))


    def test_fuel_capacity_check(self):
        self.car.fuel_capacity = 20
        self.assertEqual(20, self.car.fuel_capacity)


    def test_car_check_if_fuel_capacity_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5

            # assertion
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))


    def test_car_check_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)


    def test_car_check_if_refuel_is_zero_or_negative(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

            # assertion
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))


    def test_if_drive_furel_is_enough_to_get(self):
        self.car.fuel_amount = 20
        self.car.drive(50)
        self.assertEqual(15, self.car.fuel_amount)

    def test_if_drive_furel_is_not_enough_to_drive(self):
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(220)

            # assertion
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))



if __name__ == '__main__':
    unittest.main()