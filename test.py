import unittest

from main import score, match


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

    def test_lowercase_match_in_uppercase_location_is_zero(self):
        self.assertEqual(0, score("and", "a__", ""))

    def test_match_exact(self):
        self.assertTrue(match("relic", "RELIC", "", ""))

    def test_match_partial(self):
        self.assertTrue(match("relic", "R_L_C", "", ""))

    def test_match_includes(self):
        self.assertTrue(match("relic", "_____", "rlc", ""))

    def test_dont_match_includes_missing(self):
        self.assertFalse(match("relic", "_____", "rulc", ""))


if __name__ == '__main__':
    unittest.main()
