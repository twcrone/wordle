import unittest

from main import matches


class TestWordle(unittest.TestCase):

    def test(self):
        self.assertEqual(9, matches("bob", "bob"))

    def test_zero(self):
        self.assertEqual(0, matches("bob", "jon"))


if __name__ == '__main__':
    unittest.main()
