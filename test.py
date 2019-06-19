import unittest
import io
import sys
import lab
from point import Point

class Problem1Tests(unittest.TestCase):
    def test_01(self):
        expected = "-259.5"
        got = io.StringIO()
        sys.stdout = got
        lab.quadratic_eval(-2, -6, 0.5, 10)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())

    def test_02(self):
        expected = "233.45"
        got = io.StringIO()
        sys.stdout = got
        lab.quadratic_eval(5, 0, 9, 6.7)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())

    def test_03(self):
        expected = "-453696.8"
        got = io.StringIO()
        sys.stdout = got
        lab.quadratic_eval(0, -8.4, 4, 54012)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())


class Problem2Tests(unittest.TestCase):
    def test_01(self):
        p1 = Point(0, 0)
        p2 = Point(1, 0)
        expected = "1.0"
        got = io.StringIO()
        sys.stdout = got
        lab.find_distance(p1, p2)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())

    def test_02(self):
        p1 = Point(-1, 89)
        p2 = Point(5, -9)
        expected = "98.18"
        got = io.StringIO()
        sys.stdout = got
        lab.find_distance(p1, p2)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())

    def test_03(self):
        p1 = Point(34011, 4350)
        p2 = Point(12, 57)
        expected = "34268.96"
        got = io.StringIO()
        sys.stdout = got
        lab.find_distance(p1, p2)
        sys.stdout = sys.__stdout__
        self.assertTrue(expected in got.getvalue())


class Problem3Tests(unittest.TestCase):
    def test_01(self):
        numbers = {1, 2, 6}
        expected = 3
        got = lab.arithmetic_mean(numbers)
        self.assertEqual(got, expected)

    def test_02(self):
        numbers = {-13, 2, 10, -7, 100, 55}
        expected = 24.5
        got = lab.arithmetic_mean(numbers)
        self.assertEqual(got, expected)

    def test_03(self):
        numbers = set()
        expected = None
        got = lab.arithmetic_mean(numbers)
        self.assertEqual(got, expected)


class Problem4Tests(unittest.TestCase):
    def test_01(self):
        numbers = [1, 2, 6]
        expected = 2.2894284851066637
        got = lab.geometric_mean(numbers)
        self.assertEqual(round(got, 2), round(expected, 2))

    def test_02(self):
        numbers = [13, 2, 10, 7, 100, 55]
        expected = 14.680437989650818
        got = lab.geometric_mean(numbers)
        self.assertEqual(round(got, 2), round(expected, 2))

    def test_03(self):
        numbers = list()
        expected = None
        got = lab.geometric_mean(numbers)
        self.assertEqual(got, expected)



class Problem5Tests(unittest.TestCase):
    def test_01(self):
        numbers = [5, 10]
        expected = 5
        got = lab.second_largest_number(numbers)
        self.assertEqual(got, expected)

    def test_02(self):
        numbers = [-10, 5, 7, -100, 63, 44]
        expected = 44
        got = lab.second_largest_number(numbers)
        self.assertEqual(got, expected)

    def test_03(self):
        numbers = list()
        expected = None
        got = lab.second_largest_number(numbers)
        self.assertEqual(got, expected)


class Problem6Tests(unittest.TestCase):
    def test_01(self):
        names = ["Al", "Ted", "Richard"]
        expected = 3
        got = lab.num_unique_names(names)
        self.assertEqual(got, expected)

    def test_02(self):
        names = ["Sarah", "Jaime", "Sarah", "Sarah", "James", "Jim", "James", "Jaime", "Jeremy", "Sarah"]
        expected = 5
        got = lab.num_unique_names(names)
        self.assertEqual(got, expected)

    def test_03(self):
        names = list()
        expected = 0
        got = lab.num_unique_names(names)
        self.assertEqual(got, expected)



class Problem7Tests(unittest.TestCase):
    def test_01(self):
        d = {
            0: 1,
            1: 2,
            2: 3
        }

        expected = {
            3: 2,
            2: 1,
            1: 0
        }

        got = lab.dictionary_swap(d)
        self.assertEqual(got, expected)

    def test_02(self):
        d = {
            "first_name": "Cameron",
            "middle_name": "Brian",
            "last_name": "Smith",
            "age": 19,
            "course": "Computer Science",
            "university": "Makerere"
        }

        expected = {
            "Cameron": "first_name",
            "Brian": "middle_name",
            "Smith": "last_name",
            19: "age",
            "Computer Science": "course",
            "Makerere": "university"
        }

        got = lab.dictionary_swap(d)
        self.assertEqual(got, expected)

    def test_03(self):
        d = {}
        expected = {}
        got = lab.dictionary_swap(d)
        self.assertEqual(got, expected)


class Problem8Tests(unittest.TestCase):
    def test_01(self):
        expected = 6550000
        got = lab.electric_bill(2300)
        self.assertEqual(got, expected)

    def test_02(self):
        expected = 85750000
        got = lab.electric_bill(20500)
        self.assertEqual(got, expected)

    def test_03(self):
        expected = 0
        got = lab.electric_bill(0)
        self.assertEqual(got, expected)


class Problem9Tests(unittest.TestCase):
    def test_01(self):
        inventory = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        transaction = ("buy", "chickens", 5)

        expected = {
            "chickens": 10,
            "cows": 2,
            "pigs": 9
        }

        lab.warehouse_process(inventory, transaction)
        self.assertEqual(inventory, expected)

    def test_02(self):
        inventory = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        transaction = ("sell", "pigs", 6)

        expected = {
            "chickens": 5,
            "cows": 2,
            "pigs": 3
        }

        lab.warehouse_process(inventory, transaction)
        self.assertEqual(inventory, expected)

    def test_03(self):
        inventory = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        transaction = ("buy", "lambs", 18)

        expected = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9,
            "lambs": 18
        }

        lab.warehouse_process(inventory, transaction)
        self.assertEqual(inventory, expected)

    def test_04(self):
        inventory = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        transaction = ("sell", "cows", 0)

        expected = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        lab.warehouse_process(inventory, transaction)
        self.assertEqual(inventory, expected)

    def test_05(self):
        inventory = {
            "chickens": 5,
            "cows": 2,
            "pigs": 9
        }

        transaction = ("sell", "cows", 7)

        try:
            lab.warehouse_process(inventory, transaction)
        except ValueError:
            self.assertTrue(True)
        except:
            self.assertTrue(False)


class Problem10Tests(unittest.TestCase):
    def test_01(self):
        n = 1
        expected = 1
        got = lab.fibonacci(n)
        self.assertEqual(got, expected)

    def test_02(self):
        n = 2
        expected = 1
        got = lab.fibonacci(n)
        self.assertEqual(got, expected)

    def test_03(self):
        n = 7
        expected = 13
        got = lab.fibonacci(n)
        self.assertEqual(got, expected)


class Problem11Tests(unittest.TestCase):
    def test_01(self):
        x = 12
        expected = 10
        got = lab.hailstone(x)
        self.assertEqual(got, expected)

    def test_02(self):
        x = 19
        expected = 21
        got = lab.hailstone(x)
        self.assertEqual(got, expected)

    def test_03(self):
        x = 27
        expected = 112
        got = lab.hailstone(x)
        self.assertEqual(got, expected)


class Problem12Tests(unittest.TestCase):
    def test_01(self):
        debts = {
            "Emily" : [5, 10, 3, 11],
            "Jeremy" : [2, 7, 5, 10]
        }
        person = "Emily"
        amt = 10
        expected = {
            "Emily" : [5, 10, 3, 11, 10],
            "Jeremy" : [2, 7, 5, 10]
        }
        got = lab.borrow_money(debts, person, amt)
        self.assertEqual(got, expected)
    
    def test_02(self):
        debts = {
            "Emily" : [5, 10, 3, 11]
        }
        person = "Jeremy"
        amt = 5
        expected = {
            "Emily" : [5, 10, 3, 11],
            "Jeremy" : [5]
        }
        got = lab.borrow_money(debts, person, amt)
        self.assertEqual(got, expected)
        
    def test_03(self):
        debts = {
            "Emily" : [5, 10, 3, 11],
            "Jeremy" : [2, 7, 5, 10]
        }
        person = "Emily"
        expected = 29
        got = lab.amt_owed_by(debts, person)
        self.assertEqual(got, expected)
    
    def test_04(self):
        debts = {
            "Emily" : [5, 10, 3, 11],
            "Jeremy" : [2, 7, 5, 10]
        }
        expected = 53
        got = lab.total_amt_owed(debts)
        self.assertEqual(got, expected)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)


