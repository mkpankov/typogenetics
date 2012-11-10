#!/usr/bin/env python

"""Unit test for translation"""


import unittest
from tranlation import Translation
from enzyme import Enzyme
from strand import Strand
from binding import BindingLocation


class SimpleTranslationCheck(unittest.TestCase):
    def setUp:
        e = Enzyme(['rpu', 'ina'])
        s = Strand(list('ACGT'))
        b = BindingLocation('beginning')

    def test_translation_by_stages(self):
        t = Translation(enzyme=e, strand=s, binding_location=b)

        i = next(t.translate_by_stage())
        s_i, action, l_i, do_copy = i
        self.assertEquals(s_i, Strand(list('ACGT')))
        self.assertEquals(action, '')
        self.assertEquals(l, 0)

        i = next(t.translate_by_stage())
        s_i, action, l_i, do_copy = i
        self.assertEquals(s_i, Strand(list('ACGT')))
        self.assertEquals(action, 'rpu')
        self.assertEquals(l_i, 2)

        i = next(t.translate_by_stage())
        s_i, action, l_i, do_copy = i
        self.assertEquals(s_i, Strand(list('ACGAT')))
        self.assertEquals(action, 'ina')
        self.assertEquals(l_i, 3)

    def test_translation_iteration(self):
        t = Translation(enzyme=e, strand=s, binding_location=b)
        strands = [Strand(list('ACGT')),
                   Strand(list('ACGT')),
                   Strand(list('ACGAT'))]
        actions = ['',
                   'rpu',
                   'ina']
        locuses = [0,
                   2,
                   3]

        for i, item in enumerate(t.translate_by_stage()):
            s_i, a_i, l_i, _ = item
            self.assertEquals(s_i, strands[i])
            self.assertEquals(a_i, actions[i])
            self.assertEquals(l_i, locuses[i])

    def test_stray_aminoacid_application:
        t = Translation(enzyme=e, strand=s, binding_location=b)
        t.apply_aminoacid('cut')
        s, a, l, c = t.context
        self.assertEquals(s, [list('A CGT')])
        self.assertEquals(a, 'cut')
        self.assertEquals(l, 0)
        self.assertEquals(c, False)


if __name__ == "__main__":
    unittest.main()
