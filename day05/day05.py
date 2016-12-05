#!/usr/bin/env python
from hashlib import md5
from sys import maxsize

def main():
    input = 'cxdnnyjw'
    code = ''
    for i in range(maxsize):
        m = md5()
        m.update((input + str(i)).encode())
        s = m.hexdigest()
        if s.startswith('00000'):
            code += s[5]
            if len(code) == 8:
                print('Answer #1=' + code)


if __name__ == '__main__':
    main()