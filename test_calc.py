import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(50, 5), 55)
        self.assertEqual(calc.add(20, 5), 25)
        self.assertEqual(calc.add(15, 5), 20)
    def subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(20, 5), 15)
        self.assertEqual(calc.subtract(15, 5), 10)
        self.assertEqual(calc.subtract(11, 5), 6)
    def test_multiplay(self):
        self.assertEqual(calc.multiplay(10, 5), 50)
        self.assertEqual(calc.multiplay(10, 0), 0)
        self.assertEqual(calc.multiplay(10, 1), 10)
        self.assertEqual(calc.multiplay(10, 2), 20)
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(12, 6), 2)
        self.assertEqual(calc.divide(12, 4), 3)
        self.assertEqual(calc.divide(124, 2), 62)
        with self.assertRaises(ValueError):
            (calc.divide(10,0))


if __name__ == "__main__":
    unittest.main()