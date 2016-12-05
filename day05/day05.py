#!/usr/bin/env python
from hashlib import md5
from sys import maxsize

def main():
    input = 'cxdnnyjw'
    code = list('________')
    for i in range(maxsize):
        m = md5()
        m.update((input + str(i)).encode())
        s = m.hexdigest()
        if s.startswith('00000'):
            pos = int(s[5], 16)
            digit = s[6]
            if pos > 7:
                continue
            if code[pos] == '_':
                code[pos] = digit
            print('{} {} {}'.format(''.join(code), pos, digit))
            if not '_' in code:
                print('Answer #2=' + ''.join(code))
                return


if __name__ == '__main__':
    main()