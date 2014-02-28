#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p32.py
author: Zach Lamberty
created: 2014-02-23

Description:
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.

Notes:
    For a * b = c, the only values of a and b that yield exactly 9 total digits
    (i.e. dig(a) + dig(b) + dig(c) == 9) are:

        a, b = 1, 4
        a, b = 2, 3

    With this limited set, now let's just use generators.

"""

from itertools import product


if __name__ == '__main__':

    x = set()
    for myRange in [product(range(9), range(1000, 10000)),
                    product(range(10, 100), range(100, 1000))]:
        for (a, b) in myRange:
            c = a * b
            s = str(a) + str(b) + str(c)
            if ''.join(sorted(s)) == '123456789':
                x.add((a, b, c))

    p = {k[2] for k in x}

    print p
    print sum(p)
