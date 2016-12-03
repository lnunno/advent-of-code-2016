#!/usr/bin/env python

import os
import unittest
from day02.bathroom import get_bathroom_code, get_cross_bathroom_code

cd = os.path.dirname(os.path.realpath(__file__))

class TestCase(unittest.TestCase):
    def test_get_bathroom_code(self):
        with open(os.path.join(cd, 'test_code.txt')) as f:
            self.assertEqual('1985', get_bathroom_code(f.readlines()))
    
    def test_get_cross_bathroom_code(self):
        with open(os.path.join(cd, 'test_code.txt'))as f:
            self.assertEqual('5DB3', get_cross_bathroom_code(f.readlines()))

if __name__ == '__main__':
    unittest.main()
