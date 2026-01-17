import unittest
# This imports the add function from your lab1_3.py file
from lab1_3 import add

class TestLab1_3(unittest.TestCase):

    def test_add_positive(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """Test adding a number and zero."""
        self.assertEqual(add(10, 0), 10)

if __name__ == '__main__':
    unittest.main()
