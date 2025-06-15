# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
       
        self.calc = SimpleCalculator()
        print(f"\nSetting up a new SimpleCalculator for test: {self._testMethodName}")

    def tearDown(self):
    
        print(f"Tearing down after test: {self._testMethodName}") 

    
    def test_add_positive_numbers(self):
        """Test the addition of two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0.5, 1.5), 2.0)

    def test_add_negative_numbers(self):
        """Test the addition of two negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_positive_and_negative_numbers(self):
        """Test the addition of a positive and a negative number."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

    def test_add_with_zero(self):
        """Test addition involving zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(-5, 0), -5)
        self.assertEqual(self.calc.add(0, 0), 0)


    def test_subtract_positive_numbers(self):
        """Test the subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(10.0, 4.5), 5.5)

    def test_subtract_negative_numbers(self):
        """Test the subtraction involving negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed positive and negative numbers."""
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)


    def test_multiply_positive_numbers(self):
        """Test the multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 0.5), 5.0)

    def test_multiply_negative_numbers(self):
        """Test the multiplication of two negative numbers."""
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, -1), 5)

    def test_multiply_mixed_numbers(self):
        """Test multiplication with mixed positive and negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(5, -4), -20)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)


    def test_divide_normal_cases(self):
        """Test normal division cases."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_by_zero(self):
        """Test division by zero, which should return None as per the class spec."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # While mathematically undefined, the method returns None

    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    def test_divide_fractional_results(self):
        """Test division leading to fractional results."""
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
        # Use assertAlmostEqual for floating-point comparisons due to precision issues.


# This block allows you to run the tests directly from the script
if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 provides more detailed output