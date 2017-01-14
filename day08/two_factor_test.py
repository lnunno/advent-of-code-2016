#!/usr/bin/env python

import unittest
from day08.two_factor import make_array, rect, rotate_col, rotate_row


class TestCase(unittest.TestCase):

    def test_rotation(self):
        a = make_array(3, 7)
        rect(a, 3, 2)
        print(a)
        rotate_col(a, 1, 1)
        print(a)
        rotate_row(a, 0, 4)
        print(a)
        rotate_col(a, 1, 1)
        print(a)
        self.assertEqual(6, a.values.sum())

if __name__ == '__main__':
    unittest.main()
