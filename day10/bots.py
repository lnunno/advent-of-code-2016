#!/usr/bin/env python
import re
from typing import List

VALUE_PATTERN = re.compile(
    r'value (?P<value>\d+) goes to bot (?P<bot_num>\d+)')
GIVE_PATTERN = re.compile(
    r'bot (?P<giver>\d+) gives low to (?P<recv1_type>(?:bot|output)) (?P<recv1>\d+) and high to (?P<recv2_type>(?:bot|output)) (?P<recv2>\d+)')


class Bot(object):

    def __init__(self, number, low=None, high=None):
        self.number = number
        self.high = high
        self.low = low

    def check_for_part1_answer(self):
        if self.low == 17 and self.high == 61:
            print(
                '############Bot #{} is the answer to part1!###############'.format(
                    self.number))

    def get_input(self, i: int):
        if self.high is None:
            self.high = i
        elif i >= self.high:
            self.high, self.low = i, self.high
        elif self.low is None:
            self.low = i
        elif i <= self.low:
            self.high, self.low = self.low, i
        self.check_for_part1_answer()

    def ready(self) -> bool:
        return self.high is not None and self.low is not None

    def give_value(self, other_bot: 'Bot', value_type: str):
        self.check_for_part1_answer()
        if value_type == 'high':
            if self.high is None:
                raise Exception('Tried to give None value!')
            other_bot.get_input(self.high)
            self.high = None
        elif value_type == 'low':
            if self.low is None:
                raise Exception('Tried to give None value!')
            other_bot.get_input(self.low)
            self.low = None
        else:
            raise Exception('Unkown value_type={}'.format(value_type))

    def give_output(self, index: int, value_type: str, outputs: List[int]):
        self.check_for_part1_answer()
        if value_type == 'high':
            value = self.high
        elif value_type == 'low':
            value = self.low
        else:
            raise Exception('Unkown value_type={}'.format(value_type))
        outputs[index] = value

    def __repr__(self):
        return 'Bot(number={}, low={}, high={})'.format(
            self.number, self.low, self.high)


def get_or_add(m, index):
    if m.get(index, None) is None:
        b = Bot(index)
        m[index] = b
        return b
    else:
        return m[index]


def part1():
    with open('input.txt') as f:
        lines = []
        bots = {}  # type: Dict[int, Bot]
        for line in f.readlines():
            match = VALUE_PATTERN.match(line)
            if match:
                groupdict = match.groupdict()
                value = int(groupdict['value'])
                bot_num = int(groupdict['bot_num'])
                print('{} => bot#{}'.format(value, bot_num))
                bot = get_or_add(bots, bot_num)
                bot.get_input(value)
                print(bot)
            else:
                lines.append(line)
        outputs = [0] * 100
        processed_lines = set()  # type: Set[int]
        while len(processed_lines) != len(lines):
            for i, line in enumerate(lines):
                match = GIVE_PATTERN.match(line)
                if not match:
                    raise Exception(
                        'Line: {} did not match the give pattern!'.format(line))
                groupdict = match.groupdict()
                giver = int(groupdict['giver'])
                recv1_type = groupdict['recv1_type']
                recv1 = int(groupdict['recv1'])
                recv2_type = groupdict['recv2_type']
                recv2 = int(groupdict['recv2'])
                giver_bot = bots.get(giver, Bot(giver))
                if not giver_bot.ready():
                    continue
                print('Processing line {}'.format(line.strip()))
                print('Giver={}'.format(giver_bot))
                if recv1_type == 'output':
                    giver_bot.give_output(recv1, 'low', outputs)
                elif recv1_type == 'bot':
                    recv1_bot = get_or_add(bots, recv1)
                    giver_bot.give_value(recv1_bot, 'low')
                    print(recv1_bot)
                else:
                    raise Exception('Invalid recv1_type {}'.format(recv1_type))
                if recv2_type == 'output':
                    giver_bot.give_output(recv2, 'high', outputs)
                elif recv2_type == 'bot':
                    recv2_bot = get_or_add(bots, recv2)
                    giver_bot.give_value(recv2_bot, 'high')
                    print(recv2_bot)
                else:
                    raise Exception('Invalid recv2_type {}'.format(recv2_type))
                # Done processing line.
                processed_lines.add(i)
                print('Giver after={}'.format(giver_bot))
        print('Outputs={}'.format(outputs))


def main():
    part1()

if __name__ == '__main__':
    main()
