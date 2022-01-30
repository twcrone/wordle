import unittest

from main import score


class TestWordle(unittest.TestCase):

    def test(self):
        self.assertEqual(9, score("bob", "BOB", ""))

    def test_zero(self):
        self.assertEqual(0, score("bill", "TRAD", ""))

    def test_one_exact_match(self):
        self.assertEqual(3, score("bob", "BEN", ""))

    def test_lengths_not_equal(self):
        self.assertEqual(-1, score("bob", "BILL", ""))

    def test_one(self):
        self.assertEqual(1, score("tod", "mat", ""))

    def test_zero_when_any_excluded(self):
        self.assertEqual(0, score("bobby", "BOBB_", "y"))

    def test_zero_when_any_excludes_many(self):
        self.assertEqual(0, score("there", "___r_", "acidthe"))


if __name__ == '__main__':
    unittest.main()
