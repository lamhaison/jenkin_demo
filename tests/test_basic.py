# -*- coding: utf-8 -*-

from .context import sample

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    # def test_sum_method(self):
    #     self.assertEqual(10, 5 +6)



if __name__ == '__main__':
    unittest.main()