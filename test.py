import unittest

from main import match


class TestWordle(unittest.TestCase):

    def test_match_exact(self):
        self.assertTrue(match("relic", "RELIC", "", ""))

    def test_match_partial(self):
        self.assertTrue(match("relic", "R_L_C", "", ""))

    def test_dont_match_includes_missing(self):
        self.assertFalse(match("relic", "_____", "rulc", ""))

    def test_match_with_excludes(self):
        self.assertTrue(match("relic", "R_L_C", "ei", "x"))

    def test_no_match_with_excludes(self):
        self.assertFalse(match("relic", "R_L_C", "i", "e"))


if __name__ == '__main__':
    unittest.main()
