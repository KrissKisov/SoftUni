from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Pesho", 10_000, 100)

    def test_correct_init(self):
        self.assertEqual("Pesho", self.worker.name)
        self.assertEqual(10_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_decreases_and_money_increase_after_work_method_is_called(self):
        expected_energy = self.worker.energy - 2
        expected_money = self.worker.salary * 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_raise_exception_when_worker_works_with_no_energy(self):
        self.worker.energy = -2

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_energy_increases_after_rest_method_is_called(self):
        expected_energy = self.worker.energy + 3

        self.worker.rest()
        self.worker.rest()
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_method_returns_correct_string_and_values(self):
        expected_output = f"Pesho has saved {10_000} money."

        self.worker.work()

        self.assertEqual(expected_output, self.worker.get_info())


if __name__ == "__main__":
    main()
