#!/usr/bin/env python

"""Unit test for strand.py"""

import strand
import unittest

class BasesCheck(unittest.TestCase):
    correct_bases = frozenset(['A', 'C', 'G', 'T'])
    def test(self):
        """It should be just that set"""
        self.assertEqual(self.correct_bases, strand.bases)

class StrandTest(unittest.TestCase):
    correct_bases = frozenset(['A', 'C', 'G', 'T'])
    def testCorrectCreation(self):
        """Strand should contain correct string"""
        s = strand.Strand('ACGT')
        self.assertEqual('ACGT', s.contents)
    def testIncorrectCreationBadString(self):
        """Strand should raise an exception in case of bad string"""
        self.assertRaises(strand.IncorrectString, strand.Strand, 'BCDE')
    def testIncorrectCreationNotAString(self):
        """Strand should raise an exception in case of not a string"""
        self.assertRaises(strand.NotAString, strand.Strand, 42)
    def testRepr(self):
        s = strand.Strand('ACGT')
        self.assertEqual('Strand("ACGT")', repr(s))
    def testStr(self):
        s = strand.Strand('ACGT')
        self.assertEqual('Strand("ACGT")', str(s))

if __name__ == "__main__":
    unittest.main()
