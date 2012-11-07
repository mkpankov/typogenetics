#!/usr/bin/env python

"""Unit test for translation"""

import strand
import enzyme
import unittest
import itertools

class TranslationTest(unittest.TestCase):
    def testASimplestTranslation(self):
        """Strand is translated by enzyme to produce set of new strands"""
        string = 'ACA'
        s = strand.Strand(string)
        e = enzyme.Enzyme(['dlt', 'mvr', 'itt'], 'A')
        locus = 0
        e.attach(s, locus)
        result = next(e.translate())
        self.assertEquals(result, [list('CAT')]) 

    def testASimpleTranslation(self):
        string = 'TAGATCCAGTCCATCGA'
        s = strand.Strand(string)
        e = enzyme.Enzyme(['rpu', 'inc'], 'G')
        locus = 1
        e.attach(s, locus)
        self.assertEquals(e.locus, 8)
        result = next(e.translate())
        self.assertEquals(result, [list('TAGATCCAGTCCACTCGA')])

    def testASimpleCopyingTranslation(self):
        string = 'ACGT'
        s = strand.Strand(string)
        e = enzyme.Enzyme(['cop', 'rpy', 'rpy', 'mvl', 'mvl', 'mvl', 'off', 'ina'], 'A')
        locus = 0
        e.attach(s, locus)
        result = next(e.translate())
        self.assertEquals(result, [list('AACGT'),list('TGCA')])

    def testCorrectTranslation(self):
        """Strand is translated by enzyme to produce set of new strands"""
        string = 'TAGATCCAGTCCATCGA'
        s = strand.Strand(string)
        e = enzyme.Enzyme(['rpu', 'inc', 'cop', 'mvr', 'mvl', 'swi', 'lpu', 'itt'], 'G')
        locus = 1
        e.attach(s, locus)
        self.assertEquals(e.locus, 8)
        result = next(e.translate())
        self.assertEquals(result, [list('AGCTACACCTGACCTAGAT'),list('   ATG             ')])

    def testNotAttachedTranslation(self):
        """When enzyme isn't attached, it can't translate"""
        e = enzyme.Enzyme(['rpu'], 'A')
        i = e.translate()
        self.assertRaises(enzyme.NotAttached, next, i)

if __name__ == "__main__":
    unittest.main()
