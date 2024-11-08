"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Exercise 6
Date: 11_7_24
Challenges Encountered: Argument Parsers
"""
import unittest
from calculator import Calculator

class TestCalculatorClass(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator() #ChatGPT to help with setup

    def test_add(self):
        self.assertEqual(self.calc.add(2,5), 7)
        self.assertEqual(self.calc.add(957,231), 1188)
        self.assertEqual(self.calc.add(-17,5), -12)
        self.assertEqual(self.calc.add(-15,-23), -38)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,5), -3)
        self.assertEqual(self.calc.subtract(534,231), 303)
        self.assertEqual(self.calc.subtract(-5,-21), 16)
        self.assertEqual(self.calc.subtract(-34,5), -39)
        self.assertEqual(self.calc.subtract(15,-21), 36)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,5), 10)
        self.assertEqual(self.calc.multiply(232,521), 120872)
        self.assertEqual(self.calc.multiply(-12,5), -60)
        self.assertEqual(self.calc.multiply(-12,-13), 156)
        self.assertEqual(self.calc.multiply(14,-2), -28)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 10), 0.5)
        self.assertEqual(self.calc.divide(10,5), 2)
        self.assertEqual(self.calc.divide(520,125), 4.16)
        self.assertRaises(ValueError, self.calc.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()
