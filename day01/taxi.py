#!/usr/bin/env python

import re
from enum import IntEnum, unique


@unique
class Orientation(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    LENGTH = 4


@unique
class TurnDirection(IntEnum):
    RIGHT = 1
    LEFT = 2

    @staticmethod
    def from_char(c):
        if c == 'L':
            return TurnDirection.LEFT
        elif c == 'R':
            return TurnDirection.RIGHT
        else:
            raise Exception('Cannot parse TurnDirection from {}'.format(c))


def distance(coords):
    x, y = coords
    return abs(x) + abs(y)


class Taxi(object):
    def __init__(self):
        self.coord = (0, 0)
        self.orientation = Orientation.NORTH
        self.visited_coords = set()
        self.double_visited_coords = []

    def turn(self, d):
        if d == TurnDirection.RIGHT:
            self.orientation = (self.orientation + 1) % Orientation.LENGTH
        elif d == TurnDirection.LEFT:
            self.orientation -= 1
            if self.orientation < Orientation.NORTH:
                self.orientation = Orientation.WEST
        else:
            raise Exception('Invalid turn direction {}'.format(d))

    def move(self, amount):
        old_x, old_y = self.coord
        x, y = self.coord
        if self.orientation == Orientation.NORTH:
            y += amount
            for v in [(old_x, i) for i in range(old_y+1, y)]:
                if v in self.visited_coords:
                    d = distance(v)
                    self.double_visited_coords.append(d)
                self.visited_coords.add(v)
        elif self.orientation == Orientation.SOUTH:
            y -= amount
            for v in [(old_x, i) for i in range(old_y-1, y, -1)]:
                if v in self.visited_coords:
                    d = distance(v)
                    self.double_visited_coords.append(d)
                self.visited_coords.add(v)
        elif self.orientation == Orientation.EAST:
            x += amount
            for v in [(i, old_y) for i in range(old_x+1, x)]:
                if v in self.visited_coords:
                    d = distance(v)
                    self.double_visited_coords.append(d)
                self.visited_coords.add(v)
        elif self.orientation == Orientation.WEST:
            x -= amount
            for v in [(i, old_y) for i in range(old_x-1, x, -1)]:
                if v in self.visited_coords:
                    d = distance(v)
                    self.double_visited_coords.append(d)
                self.visited_coords.add(v)
        else:
            raise Exception("Invalid orientation {}".format(self.orientation))
        self.coord = (x, y)
        if self.coord in self.visited_coords:
            d = distance(self.coord)
            self.double_visited_coords.append(d)
        self.visited_coords.add(self.coord)


direction_pattern = re.compile(r'([R|L])(\d+)')


def manhattan_distance(direction_string, taxi=None):
    dirs = [i.strip() for i in direction_string.split(',')]
    ls = []
    for ss in dirs:
        match = direction_pattern.match(ss)
        c, num = match.groups()
        ls.append((TurnDirection.from_char(c), int(num)))
    taxi = Taxi() if taxi is None else taxi
    for turn_direction, move_amount in ls:
        taxi.turn(turn_direction)
        taxi.move(move_amount)
    answer = distance(taxi.coord)
    return answer


def visited_twice(direction_string):
    taxi = Taxi()
    manhattan_distance(direction_string, taxi)
    return taxi.double_visited_coords[0]


def main():
    with open('taxi_input.txt', 'r') as f:
        s = f.read()
        answer = manhattan_distance(s)
        print('Answer #1={}'.format(answer))
        answer = visited_twice(s)
        print('Answer #2={}'.format(answer))


if __name__ == '__main__':
    main()
