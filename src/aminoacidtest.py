#!/usr/bin/env python

"""Unit test for aminoacid.py"""

import aminoacid
import unittest
import itertools

aminoacids = {
    'cut':'s', 'dlt':'s', 'swi':'r', 'mvr':'s', 
    'mvl':'s', 'cop':'r', 'off':'l', 
    'ina':'s', 'inc':'r', 'ing':'r', 'itt':'l', 
    'rpy':'r', 'rpu':'l', 'lpy':'l', 'lpu':'l', 
}

class AminoAcidsCheck(unittest.TestCase):
    def testAminoAcidsDict(self):
        """Aminoacids is dictionary of commands mapped onto directions
        for tertiary enzyme structure"""
        self.assertEquals(aminoacid.aminoacids, aminoacids)
    def testAminoAcidCorrectCreation(self):
        """Aminoacid is successfully created from a duplet of units"""
        a = aminoacid.Aminoacid('TC')
        self.assertEquals(a.name, 'rpu')
    def testAminoAcidCorrectCreationByName(self):
        """Aminoacid is successfully created by name"""
        a = aminoacid.Aminoacid('rpu')
        self.assertEquals(a.name, 'rpu')
        self.assertIs(a.method, aminoacid.rpu)
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

class AminoAcidsRunCheck(unittest.TestCase):
    def testMvrNoCopy(self):
        strands = [list('ACGT')]
        self.assertEquals(aminoacid.mvr(strands, 1, False), 2)
    def testMvrCopy(self):
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvr(strands, 0, True), 1)
        self.assertEquals(strands, [list('ACGTAC'),list('TG    ')])
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvr(strands, 1, True), 2)
        self.assertEquals(strands, [list('ACGTAC'),list(' GC   ')])
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvr(strands, 2, True), 3)
        self.assertEquals(strands, [list('ACGTAC'),list('  CA  ')])
    def testMvlNoCopy(self):
        strands = [list('ACGT')]
        self.assertEquals(aminoacid.mvl(strands, 1, False), 0)
    def testMvlCopy(self):
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvl(strands, 1, True), 0)
        self.assertEquals(strands, [list('ACGTAC'),list('TG    ')])
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvl(strands, 2, True), 1)
        self.assertEquals(strands, [list('ACGTAC'),list(' GC   ')])
        strands = [list('ACGTAC')]
        self.assertEquals(aminoacid.mvl(strands, 3, True), 2)
        self.assertEquals(strands, [list('ACGTAC'),list('  CA  ')])
    def testRpyNoCopy(self):
        self.assertEquals(aminoacid.rpy([list('ACGTAGTC')], 2), 3)
    def testRpyCopy(self):
        strands = [list('ACGT')]
        self.assertEquals(aminoacid.rpy(strands, 0, True), 1)
        self.assertEquals(strands, [list('ACGT'),list('TG  ')])
        strands = [list('ACGT'),list('T')]
        self.assertEquals(aminoacid.rpy(strands, 0, True), 1)
        self.assertEquals(strands, [list('ACGT'),list('TG  ')])
    def testASimpleCopyingTranslationByStage(self):
        strands = [list('ACGT')]
        ['cop', 'rpy', 'rpy', 'mvl', 'mvl', 'mvl', 'off', 'ina']
        self.assertEquals(aminoacid.cop(False), True)

        self.assertEquals(aminoacid.rpy(strands, 0, True), 1)
        self.assertEquals(strands,[list('ACGT'), list('TG  ')])

        self.assertEquals(aminoacid.rpy(strands, 1, True), 3)
        self.assertEquals(strands,[list('ACGT'), list('TGCA')])

        self.assertEquals(aminoacid.mvl(strands, 3, True), 2)
        self.assertEquals(strands,[list('ACGT'), list('TGCA')])

        self.assertEquals(aminoacid.mvl(strands, 2, True), 1)
        self.assertEquals(strands,[list('ACGT'), list('TGCA')])

        self.assertEquals(aminoacid.mvl(strands, 1, True), 0)
        self.assertEquals(strands,[list('ACGT'), list('TGCA')])

        self.assertEquals(aminoacid.off(True), False)

        self.assertEquals(aminoacid.ina(strands, 0), ([list('AACGT'), list('TGCA')], 1))
        self.assertEquals(strands,[list('AACGT'), list('TGCA')])

if __name__ == "__main__":
    unittest.main()
