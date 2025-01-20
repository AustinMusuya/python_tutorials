import unittest
import time
from exercise1 import calculate_square


class TestSquare(unittest.TestCase):
    def test_square1(self):
        time.sleep(1.0)
        result = calculate_square(5)
        self.assertEqual(result, 25)

    def test_square2(self):
        time.sleep(1.0)
        result = calculate_square(-5)
        self.assertEqual(result, 25)

    def test_square3(self):
        time.sleep(1.0)
        result = calculate_square(100)
        self.assertEqual(result, 10000)

    def test_square4(self):
        time.sleep(1.0)
        result = calculate_square("5")
        self.assertIsNone(result)

    def test_square5(self):
        time.sleep(1.0)
        result = calculate_square(5.0)
        self.assertEqual(result, 25.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
