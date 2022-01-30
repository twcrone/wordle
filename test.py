import unittest

from main import score


class TestWordle(unittest.TestCase):

    def test(self):
        self.assertEqual(9, score("bob", "bob"))

    def test_zero(self):
        self.assertEqual(0, score("bill", "trad"))

    def test_one_exact_match(self):
        self.assertEqual(3, score("bob", "ben"))

    def test_lengths_not_equal(self):
        self.assertEqual(-1, score("bob", "bill"))


if __name__ == '__main__':
    unittest.main()
