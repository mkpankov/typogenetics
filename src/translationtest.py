#!/usr/bin/env python

"""Unit test for translation"""

import strand
import enzyme
import unittest
import itertools

class TranslationTest(unittest.TestCase):
	def testCorrectTranslation(self):
		"""Strand is translated by enzyme to produce set of new strands"""
		locus_string = 'TAGATCCA|GTCCATGCA'
		s = strand.Strand(locus_string.strip('|'))
		e = enzyme.Enzyme(['rpu', 'inc', 'cop', 'mvr', 'mvl', 'swi', 'lpu', 'int'])
		result = enzyme.translate(e, s, locus_string)
		self.assertEquals(result, frozenset('ACG', 'TAGATCCAGTCCACATCGA'))
		