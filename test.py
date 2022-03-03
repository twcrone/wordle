import unittest

from main import excluded, match, matches


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

    def test_not_excluded(self):
        self.assertFalse(excluded("relic", "e"))
        self.assertFalse(excluded("relic", "xe"))

    def test_dont_match_includes_missing(self):
        self.assertFalse(match("relic", "_____", "rulc", ""))

    def test_match_with_excludes(self):
        self.assertTrue(match("relic", "R_L_C", "ei", "x"))

    def test_no_match_with_excludes(self):
        self.assertFalse(match("relic", "R_L_C", "i", "e"))

    def test_match_with_ignored_include(self):
        self.assertFalse(match("relic", "R_L_C", "_", "e"))


if __name__ == '__main__':
    unittest.main()
