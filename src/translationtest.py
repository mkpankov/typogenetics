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
        e = enzyme.Enzyme(['dlt', 'mvr', 'int'], 'A')
        locus = 0
        e.attach(s, locus)
        result = list(e.translate())[0]
        self.assertEquals(result, 'CAT')        
    def testCorrectTranslation(self):
        """Strand is translated by enzyme to produce set of new strands"""
        string = 'TAGATCCAGTCCATGCA'
        s = strand.Strand(string)
        e = enzyme.Enzyme(['rpu', 'inc', 'cop', 'mvr', 'mvl', 'swi', 'lpu', 'int'], 'G')
        locus = 1
        e.attach(s, locus)
        result = e.translate()
        self.assertEquals(result, frozenset(['ACG', 'TAGATCCAGTCCACATCGA']))

    def testNotAttachedTranslation(self):
        """When enzyme isn't attached, it can't translate"""
        e = enzyme.Enzyme(['rpu'], 'A')
        self.assertRaises(enzyme.NotAttached, e.translate)

if __name__ == "__main__":
    unittest.main()
