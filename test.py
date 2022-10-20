import unittest
from maquina_cafe import CoffeeMachine

class CoffeMachineTest(unittest.TestCase):
    def test_initial(self):
        machine = CoffeeMachine()
        self.assertEqual(machine.coins, 0)

    def test_insert_coin(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        self.assertEqual(machine.coins, 1)

    def test_insert_coffee(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        self.assertEqual(machine.coffee, 1000)

    def test_insert_coffee_second_time(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        machine.insert_coffee(1000)
        self.assertEqual(machine.coffee, 2000)

    def test_insert_sugar(self):
        machine = CoffeeMachine()
        machine.insert_sugar(1000)
        self.assertEqual(machine.sugar, 1000)

    def test_insert_coffee_second_time(self):
        machine = CoffeeMachine()
        machine.insert_sugar(1000)
        machine.insert_sugar(1000)
        self.assertEqual(machine.sugar, 2000)

    def test_get_coffee_ok(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        coffee_result = machine.get_coffee()
        self.assertTrue(coffee_result)
        self.assertEqual(machine.coffee, 1000-30)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.coins, 1)

    def test_get_coffee_error_no_coffee(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_sugar(1000)
        coffee_result = machine.get_coffee()
        self.assertFalse(coffee_result)
        self.assertEqual(machine.coffee, 0)
        self.assertEqual(machine.sugar, 1000)
        self.assertEqual(machine.coins, 2)

    def test_get_coffee_error_no_sugar(self):
        machine = CoffeeMachine()
        machine.insert_coin()
        machine.insert_coin()
        machine.insert_coffee(1000)
        coffee_result = machine.get_coffee()
        self.assertFalse(coffee_result)
        self.assertEqual(machine.sugar, 0)
        self.assertEqual(machine.coffee, 1000)
        self.assertEqual(machine.coins, 2)

    def test_get_coffee_error_no_coin(self):
        machine = CoffeeMachine()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        coffee_result = machine.get_coffee()
        self.assertFalse(coffee_result)
        self.assertEqual(machine.sugar, 1000)
        self.assertEqual(machine.coffee, 1000)
        self.assertEqual(machine.coins, 0)

    def test_count_coffee_no_left(self):
        machine = CoffeeMachine()
        coffee_left = machine.count_coffee_left()
        self.assertEqual(
            coffee_left,
            0,
        )

    def test_count_coffee_no_left_because_sugar(self):
        machine = CoffeeMachine()
        machine.insert_coffee(30)
        coffee_left = machine.count_coffee_left()
        self.assertEqual(
            coffee_left,
            0,
        )

    def test_count_coffee_no_left_because_coffee(self):
        machine = CoffeeMachine()
        machine.insert_sugar(30)
        coffee_left = machine.count_coffee_left()
        self.assertEqual(
            coffee_left,
            0,
        )

    def test_count_coffee_left_1(self):
        machine = CoffeeMachine()
        machine.insert_coffee(50)
        machine.insert_sugar(5)
        coffee_left = machine.count_coffee_left()
        self.assertEqual(
            coffee_left,
            1,
        )

    def test_count_coffee_left_2(self):
        machine = CoffeeMachine()
        machine.insert_coffee(70)
        machine.insert_sugar(12)
        coffee_left = machine.count_coffee_left()
        self.assertEqual(
            coffee_left,
            2,
        )


if __name__ == '__main__':
    unittest.main()