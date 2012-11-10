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
        l = t.locus
        self.assertEquals(l, 0)
        i = next(t.translate_by_stage())
        s_i, action, l_i, do_copy = i
        print s_i, action, l_i, do_copy
        self.assertEquals(s_i, Strand(list('ACGT')))
        self.assertEquals(action, 'rpu')
        self.assertEquals(l_i, 2)
        i = next(t.translate_by_stage())
        s_i, action, l_i, do_copy = i
        print s_i, action, l_i, do_copy
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

        t = Translation(enzyme=e, strand=s, binding_location=b)

    def test_stray_aminoacid_application
        t = Translation(enzyme=e, strand=s, binding_location=b)
        

if __name__ == "__main__":
    unittest.main()
