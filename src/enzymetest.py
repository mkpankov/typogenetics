#!/usr/bin/env python

"""Unit test for enzyme.py"""

import enzyme
import unittest

class EnzymeCheck(unittest.TestCase):
    def testCorrectCreation(self):
        """Enzyme is created from an iterable with commands"""
        commands = ['cut', 'del', 'swi']
        e = enzyme.Enzyme(commands, 'A')
        self.assertEquals(e.commands, commands)
    def testTotalCreation(self):
        """Enzyme is created with all possible commands"""
        commands = ['cut', 'del', 'swi', 'mvr', 'mvl', 'cop', 'off',
                    'ina', 'inc', 'ing', 'int', 'rpy', 'rpu', 'lpy', 'lpu']
        e = enzyme.Enzyme(commands, 'A')
        self.assertEquals(e.commands, commands)
    def testIncorrectCreationStringNotInSet(self):
        self.assertRaises(enzyme.NotInSet, enzyme.Enzyme, ['aaa'], 'A')
    def testIncorrectCreationNotAString(self):
        self.assertRaises(enzyme.NotAString, enzyme.Enzyme, [42], 'A')
    def testIncorrectCreationNotIterable(self):
        self.assertRaises(TypeError, enzyme.Enzyme, 42, 'A')

class BindingCheck(unittest.TestCase):
    def testCorrectCreationSingle(self):
        """Correct binding created"""
        b = enzyme.Binding('A')
        self.assertEquals(b.binding, frozenset('A'))
    def testCorrectCreationIterable(self):
        """Correct binding created from iterable"""
        b = enzyme.Binding('AT')
        self.assertEquals(b.binding, frozenset('AT'))
    def testIncorrectCreationNotInSet(self):
        """Exception is raised when wrong string is passed"""
        self.assertRaises(enzyme.InvalidBinding, enzyme.Binding, 'BC')
    def testIncorrectCreationNotAString(self):
        """Exception is raised when not a string is passed"""
        self.assertRaises(enzyme.InvalidBinding, enzyme.Binding, 42)

if __name__ == "__main__":
    unittest.main()
