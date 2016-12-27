#!/usr/bin/env python
import numpy as np
import pandas as pd
import re
import os

RECT_PATTERN = re.compile(r'rect (?P<A>\d+)x(?P<B>\d+)')
ROTATE_PATTERN = re.compile(
    r'rotate (?P<axis>(row|column)) [y|x]=(?P<index>\d+) by (?P<amount>\d+)')


def make_array(rows=6, cols=50):
    return pd.DataFrame(np.zeros((rows, cols)))


def rect(arr, A, B):
    arr.iloc[0:B, 0:A] = 1
    return arr


def rotate_col(arr, index, amount):
    rows, _ = arr.shape
    amount = amount % (rows-1)
    s = slice((rows - amount), rows)
    temp = arr.iloc[s, index].values.copy()
    arr.iloc[:, index] = arr.iloc[:, index].shift(amount)
    arr.iloc[:amount, index] = temp
    return arr


def rotate_row(arr, index, amount):
    _, cols = arr.shape
    amount = amount % cols
    temp = arr.iloc[index, (cols - amount):cols].values.copy()
    arr.iloc[index, :] = arr.iloc[index, :].shift(amount)
    arr.iloc[index, :amount] = temp
    return arr


def part1():
    a = make_array()
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(SCRIPT_DIR, 'input.txt')) as f:
        for line in f.readlines():
            rect_match = RECT_PATTERN.match(line)
            rotate_match = ROTATE_PATTERN.match(line)
            if rect_match is not None:
                d = rect_match.groupdict()
                rect(a, int(d['A']), int(d['B']))
            elif rotate_match is not None:
                d = rotate_match.groupdict()
                axis, index, amount = d['axis'], int(d['index']), int(d['amount'])
                if axis == 'row':
                    rotate_row(a, index, amount)
                elif axis == 'column':
                    rotate_col(a, index, amount)
                else:
                    raise Exception('Unknown axis ' + axis)
            else:
                raise Exception('Could not parse line: "{}"'.format(line))
    print(a.values.sum())
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', 1000)
    text = a.copy()
    text = text.replace(0, ' ')
    text = text.replace(1, '#')
    print(text)



def main():
    part1()

if __name__ == '__main__':
    main()
