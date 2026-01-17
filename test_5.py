import unittest
# Import the functions from lab1_5.py
from lab1_5 import check_multiple, check_password, calculate_federal_tax

class TestLab1_5(unittest.TestCase):

    # 1. Tests for check_multiple
    def test_multiple_of_both(self):
        """Test a number that is a multiple of both 3 and 5 (15)."""
        self.assertTrue(check_multiple(15))

    def test_multiple_of_one(self):
        """Test a number that is only a multiple of 3 (9)."""
        self.assertFalse(check_multiple(9))

    def test_not_a_multiple(self):
        """Test a number that is a multiple of neither (7)."""
        self.assertFalse(check_multiple(7))

    # 2. Tests for check_password
    def test_password_correct(self):
        """Test the correct secret word."""
        self.assertEqual(check_password("Python123"), "access granted")

    def test_password_incorrect(self):
        """Test an incorrect password."""
        self.assertEqual(check_password("WrongPassword"), "access denied")

    # 3. Tests for calculate_federal_tax
    def test_low_bracket(self):
        """Test the 10% bracket (Salary: 10,000)."""
        self.assertEqual(calculate_federal_tax(10000), 1000.0)

    def test_mid_bracket(self):
        """Test the 22% bracket (Salary: 50,000)."""
        # 50,000 * 0.22 = 11,000
        self.assertAlmostEqual(calculate_federal_tax(50000), 11000.0)

    def test_high_bracket(self):
        """Test the 24% bracket (Salary: 100,000)."""
        # 100,000 * 0.24 = 24,000
        self.assertAlmostEqual(calculate_federal_tax(100000), 24000.0)

if __name__ == '__main__':
    unittest.main()
