#!/usr/bin/env python
import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    # part1()
    part2()

def part1():
    d = pd.DataFrame()
    for line in open(os.path.join(SCRIPT_DIR,'input.txt')).readlines():
        d = d.append(pd.Series(list(line))[:-1], ignore_index=True)
    print(d.mode(axis=0))

def part2():
    d = pd.DataFrame()
    for line in open(os.path.join(SCRIPT_DIR,'input.txt')).readlines():
        d = d.append(pd.Series(list(line))[:-1], ignore_index=True)
    for column_label in d:
        column = d[column_label]
        value_counts = column.value_counts()
        print(value_counts.idxmin())

if __name__ == '__main__':
    main()