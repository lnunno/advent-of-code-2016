#!/usr/bin/env python

num_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

cross_pad = [
    ['0', '0', '1', '0', '0'],
    ['0', '2', '3', '4', '0'],
    ['5', '6', '7', '8', '9'],
    ['0', 'A', 'B', 'C', '0'],
    ['0', '0', 'D', '0', '0'],
]

def get_bathroom_code(lines):
    x, y = (1, 1)
    start_index = (x, y)
    s = ''
    for line in lines:
        for char in line.strip():
            if char == 'U':
                y = max(0, y-1)
            elif char == 'D':
                y = min(2, y+1)
            elif char == 'R':
                x = min(2, x+1)
            elif char == 'L':
                x = max(0, x-1)
            else:
                raise Exception('Invalid direction {}'.format(char))
        s += str(num_pad[y][x])
    return s

def get_cross_bathroom_code(lines):
    x, y = (0, 2)
    start_index = (x, y)
    s = ''
    for line in lines:
        for char in line.strip():
            if char == 'U':
                ny = max(0, y-1)
                y = ny if cross_pad[ny][x] != '0' else y
            elif char == 'D':
                ny = min(4, y+1)
                y = ny if cross_pad[ny][x] != '0' else y
            elif char == 'R':
                nx = min(4, x+1)
                x = nx if cross_pad[y][nx] != '0' else x
            elif char == 'L':
                nx = max(0, x-1)
                x = nx if cross_pad[y][nx] != '0' else x
            else:
                raise Exception('Invalid direction {}'.format(char))
        s += str(cross_pad[y][x])
    return s

def main():
    with open('bathroom_code.txt') as f:
        lines = f.readlines()
        print('Answer #1=' + get_bathroom_code(lines))
        print('Answer #2=' + get_cross_bathroom_code(lines))


if __name__ == '__main__':
    main()
