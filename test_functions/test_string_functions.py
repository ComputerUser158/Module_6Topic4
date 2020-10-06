import unittest
from more_functions import string_functions


class TestMultiplyString(unittest.TestCase):
    def test_multiply_string(self):
        result = string_functions.multiply_string("ayah", 3)
        self.assertEqual(result, "ayahayahayah")


if __name__ == '__main__':
    unittest.main()
