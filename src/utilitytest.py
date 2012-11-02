#!/usr/bin/env python

"""Unit test for utility.py"""

import utility
import unittest

class StringCharsIndicesCheck(unittest.TestCase):
    def testCorrectRun(self):
        self.assertEquals(utility.string_chars_indices('ABCDABCD'), 
            {'A': [0, 4], 'B': [1, 5], 'C': [2, 6], 'D': [3, 7]})

if __name__ == "__main__":
    unittest.main()
