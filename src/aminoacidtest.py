#!/usr/bin/env python

"""Unit test for aminoacid.py"""

import aminoacid
import unittest
import itertools

aminoacids = {
    'cut':'s', 'dlt':'s', 'swi':'r', 'mvr':'s', 
    'mvl':'s', 'cop':'r', 'off':'l', 
    'ina':'s', 'inc':'r', 'ing':'r', 'int':'l', 
    'rpy':'r', 'rpu':'l', 'lpy':'l', 'lpu':'l', 
}

class AminoAcidsCheck(unittest.TestCase):
    def testAminoAcidsDict(self):
        """Aminoacids is dictionary of commands mapped onto directions
        for tertiary enzyme structure"""
        self.assertEquals(aminoacid.aminoacids, aminoacids)
    def testAminoAcidCorrectCreation(self):
        """Aminoacid is successfully created from a duplet of units"""
        a = aminoacid.Aminoacid('AC')
        self.assertEquals(a.name, 'cut')
    def testAminoAcidCorrectCreationByName(self):
        """Aminoacid is successfully created by name"""
        a = aminoacid.Aminoacid('rpu')
        self.assertEquals(a.name, 'rpu')
    def testAminoAcidSaneCreation(self):
        """Aminoacid is created from any correct duplet"""
        for tup in itertools.product('ACGT', repeat=2):
            string = ''.join(tup)
            a = aminoacid.Aminoacid(string)
            self.assertEquals(a.name, aminoacid.names[string])
    def testAminoAcidSaneCreationByName(self):
        """Aminoacid is created by any correct name"""
        for name in aminoacids.keys():
            a = aminoacid.Aminoacid(name)
            self.assertEquals(a.name, name)
    def testAminoAcidIncorrectCreationNotInSet(self):
        """Exception is raised when incorrect string is supplied"""
        self.assertRaises(aminoacid.NotInSet, aminoacid.Aminoacid, 'AB')
        self.assertRaises(aminoacid.NotInSet, aminoacid.Aminoacid, 'A')
        self.assertRaises(aminoacid.NotInSet, aminoacid.Aminoacid, 'A ')
        self.assertRaises(aminoacid.NotInSet, aminoacid.Aminoacid, 'aaa')
        self.assertRaises(aminoacid.NotInSet, aminoacid.Aminoacid, 'cat')
    def testAminoAcidIncorrectCreationNotAString(self):
        """Exception is raised when not a string is supplied"""
        self.assertRaises(aminoacid.NotAString, aminoacid.Aminoacid, 42)

if __name__ == "__main__":
    unittest.main()
