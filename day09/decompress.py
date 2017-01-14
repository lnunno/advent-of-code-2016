#!/usr/bin/env python
import re

MARKER_PATTERN = re.compile(r'\((?P<chars>\d+)x(?P<repeat>\d+)\)')


def part1():
    with open('input.txt') as f:
        s = f.read().strip()
        print(s)
        print(len(s))
        decompressed_str = decompress(s)
        print(decompressed_str)
        print(len(decompressed_str))


def part2():
    with open('input.txt') as f:
        s = f.read().strip()
        print(s)
        print(len(s))
        decompressed_str = decompress(s)
        print(decompressed_str)
        print(len(decompressed_str))


def main():
    part1()


def decompress(s: str) -> str:
    decompressed_str = ''
    match = MARKER_PATTERN.search(s)
    while match:
        groupdict = match.groupdict()
        chars = int(groupdict['chars'])
        repeat = int(groupdict['repeat'])
        decompressed_str += s[0:match.start()]
        decompressed_str += s[match.end():match.end() + chars] * repeat
        s = s[match.end() + chars:]
        match = MARKER_PATTERN.search(s)
    decompressed_str += s
    return decompressed_str


if __name__ == '__main__':
    main()
