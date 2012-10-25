#!/usr/bin/env python

"""Unit test for enzyme.py"""

import enzyme
import unittest

class AminoAcidsCheck(unittest.TestCase):
    def testAminoAcidsSet(self):
        """Aminoacids is fixed set of commands"""
        aminoacids = frozenset(
            [
                'cut', 'del', 'swi', 'mvr', 'mvl', 'cop', 'off', 
                'ina', 'inc', 'ing', 'int', 'rpy', 'rpu', 'lpy', 'lpu', 
            ]
        )
        self.assertEquals(enzyme.aminoacids, aminoacids)

class EnzymeCheck(unittest.TestCase):
    def testCorrectCreation(self):
        """Enzyme is created from an iterable with commands"""
        commands = ['cut', 'del', 'swi']
        e = enzyme.Enzyme(commands)
        self.assertEquals(e.commands, commands)
    def testTotalCreation(self):
        """Enzyme is created with all possible commands"""
        commands = ['cut', 'del', 'swi', 'mvr', 'mvl', 'cop', 'off',
                    'ina', 'inc', 'ing', 'int', 'rpy', 'rpu', 'lpy', 'lpu']
        e = enzyme.Enzyme(commands)
        self.assertEquals(e.commands, commands)
    def testIncorrectCreationStringNotInSet(self):
        self.assertRaises(enzyme.NotInSet, enzyme.Enzyme, ['aaa'])
    def testIncorrectCreationNotAString(self):
        self.assertRaises(enzyme.NotAString, enzyme.Enzyme, [42])
    def testIncorrectCreationNotIterable(self):
        self.assertRaises(TypeError, enzyme.Enzyme, 42)


if __name__ == "__main__":
    unittest.main()
