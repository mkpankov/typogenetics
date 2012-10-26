#!/usr/bin/env python

"""Unit test for aminoacid.py"""

import aminoacid
import unittest

class AminoAcidsCheck(unittest.TestCase):
    def testAminoAcidsDict(self):
        """Aminoacids is dictionary of commands mapped onto directions
        for tertiary enzyme structure"""
        aminoacids = {
            'cut':'s', 'del':'s', 'swi':'r', 'mvr':'s', 
            'mvl':'s', 'cop':'r', 'off':'l', 
            'ina':'s', 'inc':'r', 'ing':'r', 'int':'l', 
            'rpy':'r', 'rpu':'l', 'lpy':'l', 'lpu':'l', 
        }
        self.assertEquals(enzyme.aminoacids, aminoacids)