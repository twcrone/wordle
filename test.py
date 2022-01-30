import unittest

from main import score


class TestWordle(unittest.TestCase):

    def test(self):
        self.assertEqual(9, score("bob", "BOB"))

    def test_zero(self):
        self.assertEqual(0, score("bill", "TRAD"))

    def test_one_exact_match(self):
        self.assertEqual(3, score("bob", "BEN"))

    def test_lengths_not_equal(self):
        self.assertEqual(-1, score("bob", "BILL"))

    def test_one(self):
        self.assertEqual(1, score("tod", "mat"))

    def test_zero_when_any_excluded(self):
        self.assertEqual(0, score("bobby", "BOBB_", "y"))


if __name__ == '__main__':
    unittest.main()
