import unittest
import time
from palindrome import is_palindrome


class Test_is_palindrome(unittest.TestCase):
    def test_not_palindrome(self):
        time.sleep(1.0)
        result = is_palindrome(3154)
        self.assertEqual(result, False)

    def test_negative_number(self):
        time.sleep(1.0)
        result = is_palindrome(-555)
        self.assertEqual(result, False)

    def test_palindrome(self):
        time.sleep(1.0)
        result = is_palindrome(121)
        self.assertEqual(result, True)

    def test_palindrome2(self):
        time.sleep(1.0)
        result = is_palindrome(123454321)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
