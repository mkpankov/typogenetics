#!/usr/bin/env python

"""Unit test for enzyme.py"""

import enzyme
import strand
import utility
import unittest


class EnzymeCreationCheck(unittest.TestCase):
    def testCorrectCreation(self):
        """Enzyme is created from an iterable with commands"""
        commands = ['cut', 'dlt', 'swi']
        e = enzyme.Enzyme(commands, 'A')
        self.assertEquals(e.commands, commands)
    
    def testTotalCreation(self):
        """Enzyme is created with all possible commands"""
        commands = ['cut', 'dlt', 'swi', 'mvr', 'mvl', 'cop', 'off',
                    'ina', 'inc', 'ing', 'itt', 'rpy', 'rpu', 'lpy', 'lpu']
        e = enzyme.Enzyme(commands, 'A')
        self.assertEquals(e.commands, commands)
    
    def testIncorrectCreationStringNotInSet(self):
        self.assertRaises(enzyme.NotInSet, enzyme.Enzyme, ['aaa'], 'A')
    
    def testIncorrectCreationNotAString(self):
        self.assertRaises(enzyme.NotAString, enzyme.Enzyme, [42], 'A')
    
    def testIncorrectCreationNotIterable(self):
        self.assertRaises(TypeError, enzyme.Enzyme, 42, 'A')


class EnzymeAttachCheck(unittest.TestCase):
    def testCorrectRun(self):
        """Successfull attachment should set strand and locus"""
        string = 'TAGATCCAGTCCATGCA'
        s = strand.Strand(string)
        binding = 'G'
        e = enzyme.Enzyme(['itt'], binding)
        d = utility.string_chars_indices(string)
        locus = 1  # Sets index of unit to bind to
        e.attach(s, locus)
        self.assertEquals(e.locus, d[binding][locus])
        self.assertEquals(e.strand, s)
        self.assertEquals(e.status, 'attached')
    
    def testIncorrectRun(self):
        """Invalid attachment should raise exception"""
        string = 'TAGATCCATCCATCA'  # Only one 'G'
        s = strand.Strand(string)
        binding = 'G'
        e = enzyme.Enzyme(['itt'], binding)
        d = utility.string_chars_indices(string)
        locus = 1  # Sets index of unit to bind to; second 'G' assumed
        self.assertRaises(enzyme.InvalidLocus, e.attach, s, locus)


class BindingCheck(unittest.TestCase):
    def testCorrectCreationSingle(self):
        """Correct binding created"""
        b = enzyme.Binding('A')
        self.assertEquals(b.value, frozenset('A'))
    
    def testCorrectCreationIterable(self):
        """Correct binding created from iterable"""
        b = enzyme.Binding('AT')
        self.assertEquals(b.value, frozenset('AT'))
    
    def testIncorrectCreationNotInSet(self):
        """Exception is raised when wrong string is passed"""
        self.assertRaises(enzyme.InvalidBinding, enzyme.Binding, 'BC')
    
    def testIncorrectCreationNotAString(self):
        """Exception is raised when not a string is passed"""
        self.assertRaises(enzyme.InvalidBinding, enzyme.Binding, 42)

if __name__ == "__main__":
    unittest.main()
