#!/usr/bin/env python
import pandas as pd
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ABBA_PATTERN = re.compile(r'(?P<a>[a-z])(?P<b>(?!(?P=a))[a-z])(?P=b)(?P=a)')
HYPERNET_PATTERN = re.compile(r'\[(?P<hyper>[a-z]+)\]')

ABA_PATTERN = re.compile(r'(?P<a>[a-z])(?P<b>(?!(?P=a))[a-z])(?P=a)')


def supports_tls(s):
    for hyper_text in HYPERNET_PATTERN.findall(s):
        if is_abba_pattern(hyper_text):
            return False
    no_hyper = HYPERNET_PATTERN.sub(' ', s)
    non_hyper_text = no_hyper.split()
    for t in non_hyper_text:
        if is_abba_pattern(t):
            return True
    return False


def supports_ssl(s):
    aba_patterns = []
    for hyper_text in HYPERNET_PATTERN.finditer(s):
        aba_patterns.extend(ABA_PATTERN.finditer(hyper_text.group(0)))
    if len(aba_patterns) == 0:
        return False
    no_hyper = HYPERNET_PATTERN.sub(' ', s)
    non_hyper_text = no_hyper.split()
    for nh in non_hyper_text:
        for ap in aba_patterns:
            pattern = get_bab_pattern(ap.groupdict()['a'], ap.groupdict()['b'])
            if pattern.search(nh) is not None:
                print('Pattern: {}, Text: {}'.format(pattern.pattern, nh))
                return True
    return False


def get_bab_pattern(a, b):
    return re.compile('{b}{a}{b}'.format(a=a, b=b))


def is_abba_pattern(s):
    return ABBA_PATTERN.search(s) is not None


def main():
    part1()
    part2()


def part1():
    count = 0
    for line in open(os.path.join(SCRIPT_DIR, 'input.txt')).readlines():
        if supports_tls(line):
            print('Supports TLS: {}'.format(line))
            count += 1
    print(count)


def part2():
    count = 0
    for line in open(os.path.join(SCRIPT_DIR, 'input.txt')).readlines():
        if supports_ssl(line):
            print('Supports SSL: {}'.format(line))
            count += 1
    print(count)

if __name__ == '__main__':
    main()
