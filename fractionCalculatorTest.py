import unittest
from fractionCalculator import *


class TestFractionCalculator(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual('1_7/8', calculate('1/2 * 3_3/4'))
        self.assertEqual('3_1/2', calculate('2_3/8 + 9/8'))
        self.assertEqual('4_1/8', calculate('1_3/4 + 2_3/8'))

    def test_convert_to_improper(self):
        self.assertEqual('35/4', convert_to_improper('8', '3/4'))

    def test_get_operands(self):
        self.assertEqual('55/8', get_operands('6_7/8'))

    def test_get_numerator_and_denominator(self):
        self.assertEqual(('3', '4'), get_numerator_and_denominator('3/4'))

    def test_get_return_result(self):
        self.assertEqual('6_7/8', format_result('55/8'))
        self.assertEqual('7/8', format_result('7/8'))


if __name__ == '__main__':
    unittest.main()
