#!/usr/bin/env python

"""Unit test for enzyme.py"""

import enzyme
import unittest

class EnzymeCheck(unittest.TestCase):
	def testCorrectCreation(self):
		"""Enzyme is created from an iterable with commands"""
		commands = ['cut', 'del', 'swi']
		e = enzyme.Enzyme(commands)
		self.assertEquals(e.commands, commands)

if __name__ == "__main__":
    unittest.main()
