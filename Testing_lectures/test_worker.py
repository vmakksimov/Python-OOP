from Testing.worker import Worker

import unittest

class WorkerTest(unittest.TestCase):
    #def setUp(self):
        #self.worker = Worker('Test', 100, 10)
        #ako se povtarq kakto v sluchaq i posle 'worker.name,salary se zamenq s 'self.worker.name,salary)

    def test_worker_is_initialized_correctly(self):
        worker = Worker('Test', 100, 10)

        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)


    def test_worker_energy_increased_after_rest(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)


        worker.rest()
        self.assertEqual(11, worker.energy)


    def test_if_worker_works_with_negative_energy(self):
        #arrange
        worker = Worker('Test', 100, 0)


        #act
        with self.assertRaises(Exception) as ex:
            worker.work()

        #assertion
        self.assertEqual('Not enough energy.', str(ex.exception))


    def test_if_worker_moneys_increased_by_salary(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(100, worker.money)



    def test_if_worker_energy_decreased_after_work(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)


        worker.work()

        self.assertEqual(9, worker.energy)


    def test_get_info(self):
        worker = Worker('Test', 100, 10)

        actual = worker.get_info()
        expected = 'Test has saved 0 money.'


        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

