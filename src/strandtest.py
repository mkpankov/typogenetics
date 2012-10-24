#!/usr/bin/env python

"""Unit test for strand.py"""

import strand
import unittest

class BasesCheck(unittest.TestCase):
    correct_bases = set(['A', 'C', 'G', 'T'])
    def test(self):
        """It should be just that set"""
        self.assertEqual(self.correct_bases, strand.bases)

if __name__ == "__main__":
    unittest.main()
