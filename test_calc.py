import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
    def subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
    def test_multiplay(self):
        self.assertEqual(calc.multiplay(10, 5), 50)
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()