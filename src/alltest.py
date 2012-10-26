#!/usr/bin/env python

"""Testing script which invokes all sub-tests"""

from strandtest import *
from enzymetest import *
from aminoacidtest import *

import unittest

if __name__ == "__main__":
    unittest.main()
