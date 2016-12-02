#!/usr/bin/env python

import unittest
from bathroom import get_bathroom_code, get_cross_bathroom_code


class TestCase(unittest.TestCase):
    def test_get_bathroom_code(self):
        with open('test_code.txt') as f:
            self.assertEqual('1985', get_bathroom_code(f.readlines()))
    
    def test_get_cross_bathroom_code(self):
        with open('test_code.txt') as f:
            self.assertEqual('5DB3', get_cross_bathroom_code(f.readlines()))

if __name__ == '__main__':
    unittest.main()
