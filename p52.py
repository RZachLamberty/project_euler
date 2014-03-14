#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p52.py
author: Zach Lamberty
created: 2014-03-13

Description:
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.

Notes:
    The search range can be trimmed (1EN / 6 = ...) and beyond that (I assume
    it won't work)

"""

if __name__ == '__main__':

    found = False
    x = 0
    n = 1
    xJump = 10 / 6.
    while not found:
        x += 1
        sx = str(x)
        found = all([sorted(sx) == sorted(str(i * x)) for i in range(2, 7)])
        if x > xJump:
            x = int(xJump * 6)
            xJump *= 10
            print 'Just jumped to {}'.format(x)

    print 'x = {}'.format(x)
