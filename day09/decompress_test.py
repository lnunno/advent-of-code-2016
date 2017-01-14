#!/usr/bin/env python
import os
import unittest
from day09.decompress import decompress


class TestCase(unittest.TestCase):

    def test_decompress(self):
        self.assertEqual('ADVENT', decompress('ADVENT'))
        self.assertEqual('ABBBBBC', decompress('A(1x5)BC'))
        self.assertEqual('XYZXYZXYZ', decompress('(3x3)XYZ'))
        self.assertEqual('(1x3)A', decompress('(6x1)(1x3)A'))
        self.assertEqual('X(3x3)ABC(3x3)ABCY', decompress('X(8x2)(3x3)ABCY'))
        self.assertEqual('ABCABC', decompress('(3x1)ABC(5x1)ABC'))
        self.assertEqual('ABC(5x1)ABC', decompress('(4x1)ABC(5x1)ABC'))

if __name__ == '__main__':
    unittest.main()
