#!/usr/bin/env python

import os
import unittest
from day04.checksum import is_real_room, get_checksum, decode_shift_cipher

cd = os.path.dirname(os.path.realpath(__file__))

class TestCase(unittest.TestCase):

    def test_is_real_room(self):
        self.assertEqual(True, is_real_room('aaaaa-bbb-z-y-x-123[abxyz]'))
        self.assertEqual(True, is_real_room('a-b-c-d-e-f-g-h-987[abcde]'))
        self.assertEqual(True, is_real_room('not-a-real-room-404[oarel]'))
        self.assertEqual(False, is_real_room('totally-real-room-200[decoy]'))

    def test_get_checksum(self):
        self.assertEqual(123, get_checksum('aaaaa-bbb-z-y-x-123[abxyz]'))
        self.assertEqual(987, get_checksum('a-b-c-d-e-f-g-h-987[abcde]'))
        self.assertEqual(404, get_checksum('not-a-real-room-404[oarel]'))
        self.assertEqual(200, get_checksum('totally-real-room-200[decoy]'))
    
    def test_decode_shift_cipher(self):
        self.assertEqual('very encrypted name', decode_shift_cipher('qzmt-zixmtkozy-ivhz-343[abcd]'))

if __name__ == '__main__':
    unittest.main()
