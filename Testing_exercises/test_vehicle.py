from project.vehicle import Vehicle

import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(fuel=60.5, horse_power=197.5)

    def test_check_if_initiliazied_correctly(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.assertEqual(197.5, self.vehicle.horse_power)
        self.assertEqual(60.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_check_if_drive_is_possible(self):
        self.vehicle.fuel = 60.5
        self.vehicle.drive(30)
        self.assertEqual(23, self.vehicle.fuel)

    def test_check_if_drive_is_not_possible(self):
        self.vehicle.fuel = 60.5
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

            # assertion
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_check_if_refuel_is_possible(self):
        self.vehicle.fuel -= 20
        self.vehicle.refuel(10)
        self.assertEqual(50.5, self.vehicle.fuel)

    def test_check_if_refuel_is_not_possible(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

            # assertion
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_repr_is_correct(self):
        actual = self.vehicle.__str__()
        expected = "The vehicle has 197.5 " \
                   "horse power with 60.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
