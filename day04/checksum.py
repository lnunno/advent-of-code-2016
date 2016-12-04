#!/usr/bin/env python
import re
import string
from collections import Counter, OrderedDict

checksum_pattern = re.compile(r'(?P<name>[a-z\-]+)(?P<id>\d+)\[(?P<checksum>[a-z]+)\]')

def is_real_room(s):
    match = checksum_pattern.match(s)
    d = match.groupdict()
    name = d['name']
    name = name.replace('-', '')
    counter = Counter(name)
    checksum_letters = d['checksum']
    for (w, count), chk in zip(sorted(counter.items(), key=lambda x: (-x[1], x[0])), checksum_letters):
        if w != chk:
            return False
    return True

def get_checksum(s):
    match = checksum_pattern.match(s)
    d = match.groupdict()
    return int(d['id'])

def sum_of_sector_ids(lines):
    s = 0
    for line in lines:
        if is_real_room(line):
            s += get_checksum(line)
    return s

def shift_letter(letter, amount):
    lowercase_characters = list(string.ascii_lowercase)
    return lowercase_characters[(lowercase_characters.index(letter) + amount) % 26]

def decode_shift_cipher(s):
    chk = get_checksum(s)
    match = checksum_pattern.match(s)
    d = match.groupdict()
    name = d['name']
    name = name.replace('-', ' ').rstrip()
    decoded_name = ''
    for c in list(name):
        if c != ' ':
            decoded_name += shift_letter(c, chk)
        else:
            decoded_name += ' '
    return decoded_name


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        print('Answer #1={}'.format(sum_of_sector_ids(lines)))
    with open('input.txt') as f:
        lines = f.readlines()
        for i in lines:
            print('{} -> {}'.format(i.strip(), decode_shift_cipher(i)))

        

if __name__ == '__main__':
    main()