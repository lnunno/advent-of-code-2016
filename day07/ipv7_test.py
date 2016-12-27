#!/usr/bin/env python

import os
import unittest
from day07.ipv7 import supports_tls, supports_ssl


class TestCase(unittest.TestCase):

    def test_tls(self):
        self.assertEqual(True, supports_tls('abba[mnop]qrst'))
        self.assertEqual(False, supports_tls('abcd[bddb]xyyx'))
        self.assertEqual(False, supports_tls('aaaa[qwer]tyui'))
        self.assertEqual(True, supports_tls('ioxxoj[asdfgh]zxcvbn'))

    def test_ssl(self):
        self.assertTrue(supports_ssl('aba[bab]xyz'))
        self.assertFalse(supports_ssl('xyx[xyx]xyx'))
        self.assertTrue(supports_ssl('aaa[kek]eke'))
        self.assertTrue(supports_ssl('zazbz[bzb]cdb'))
        self.assertFalse(supports_ssl('aaa[aaa]aaa'))
        self.assertTrue(supports_ssl('aaa[kek]aaa[abcd]eke'))

if __name__ == '__main__':
    unittest.main()
