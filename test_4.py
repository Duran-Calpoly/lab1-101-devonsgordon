import unittest
# Import the functions from lab1_4.py
from lab1_4 import calculate_average, add_tax, greet_user

class TestLab1_4(unittest.TestCase):

    # Tests for calculate_average
    def test_average_integers(self):
        """Test average with three whole numbers."""
        self.assertEqual(calculate_average(10, 20, 30), 20.0)

    def test_average_floats(self):
        """Test average with decimal numbers."""
        self.assertAlmostEqual(calculate_average(1.5, 2.5, 5.0), 3.0)

    # Tests for add_tax
    def test_tax_calculation(self):
        """Test that 10% tax is added correctly to $100."""
        self.assertAlmostEqual(add_tax(100), 110.0)

    def test_tax_small_amount(self):
        """Test tax on a smaller amount."""
        self.assertAlmostEqual(add_tax(10), 11.0)

    # Tests for greet_user
    def test_greeting(self):
        """Test that the name is correctly inserted into the string."""
        self.assertEqual(greet_user("Alice"), "Hello Alice")

    def test_greeting_empty(self):
        """Test greeting with an empty string."""
        self.assertEqual(greet_user(""), "Hello ")

if __name__ == '__main__':
    unittest.main()
