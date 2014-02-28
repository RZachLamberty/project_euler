#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p9.py
author: Zach Lamberty
created: 2014-02-13

Description:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,

        a**2 + b**2 = c**2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

Notes:
    Given a, b:

    we want to see: (1000 - a - b)**2 == a**2 + b**2


"""

if __name__ == '__main__':

    for a in range(333):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if c**2 == a**2 + b**2:
                print 'a = {}\nb = {}\nc = {}'.format(a, b, c)
                print 'abc = {}'.format(a * b * c)
