#!/usr/bin/env python
import pandas as pd

def is_triangle(a, b, c):
    return max(a,b,c) < a + b + c - max(a,b,c)

def part1():
    with open('input.txt') as f:
        num_valid = 0
        lines = f.readlines()
        for line in lines:
            a, b, c = line.split()
            a, b, c = int(a), int(b), int(c)
            if is_triangle(a, b, c):
                num_valid += 1
        print('Answer #1={}'.format(num_valid))

def part2():
    df = pd.read_csv('input.txt', header=None, delim_whitespace=True)
    num_valid = 0
    for label in df:
        col = df[label]
        for a, b, c in zip(col[0::3], col[1::3], col[2::3]):
            if is_triangle(a, b, c):
                num_valid += 1
    print('Answer #2={}'.format(num_valid))


def main():
    part1()
    part2()

if __name__ == '__main__':
    main()