import unittest

from main import excluded, matches


class TestWordle(unittest.TestCase):

    def test_matches(self):
        self.assertTrue(matches("relic", "RELIC"))
        self.assertTrue(matches("relic", "R_L_C"))
        self.assertTrue(matches("relic", "_r_lc"))
        self.assertTrue(matches("relic", "_____"))

    def test_no_matches(self):
        self.assertFalse(matches("relic", "ABCDE"))
        self.assertFalse(matches("relic", "RAL_C"))
        self.assertFalse(matches("relic", "_a_lc"))
        self.assertFalse(matches("relic", "CILER"))

    def test_excluded(self):
        self.assertTrue(excluded("relic", "abd"))
        self.assertTrue(excluded("relic", "xyz"))


if __name__ == '__main__':
    unittest.main()
