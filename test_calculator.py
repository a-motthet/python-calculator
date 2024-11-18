import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 6), 7)
    def test_add2(self):
        self.assertEqual(self.calc.add(6, -10), -4)
    def test_add3(self):
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 1), 3)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(2, -8), 10)
    def test_subtract3(self):
        self.assertEqual(self.calc.subtract(-7, -5), -2)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 3), 21)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(7, -3), -21)
    def test_multiply3(self):
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_divide2(self):
         self.assertEqual(self.calc.divide(2, -2), -4)
    def test_divide3(self):
        self.assertEqual(self.calc.divide(-4, -4), 1)
    def test_divide4(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, -3), -2)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)
    def test_modulo3(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()