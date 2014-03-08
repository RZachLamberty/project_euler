#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p39.py
author: Zach Lamberty
created: 2014-03-02

Description:
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?

Notes:
    Here are the facts re: the solution p that we know:

        (a, b, c) are such that:

            1.  a + b + c = p
                        c = p - a - b

            2.  a**2 + b**2 = c**2
                          c = sqrt(a**2 + b**2)

            3. a, b, and c are all integers

    Combining (1) and (2), we have that

        a**2 + b**2 = (p - a - b)**2
        a**2 + b**2 = p**2 + a**2 + b**2 - 2pa - 2pb + 2ab
                  0 = p**2 -2p(a + b) + 2ab

    I did this by hand. this yields roots of

        p = a + b +- |c|

    Instead, just kind of brute force it.

"""

from collections import defaultdict
from math import sqrt


P = 1000


def is_int(n):
    """ what's the best way to check if something is an integer """
    return int(n) == n


if __name__ == '__main__':

    x = defaultdict(list)

    for a in range(1, P/3 + 1):
        for b in range(a + 1, (P - a) / 2 + 1):
            c = sqrt(a**2 + b**2)
            if is_int(c):
                x[a + b + int(c)].append((a, b, int(c)))

    print max((el for el in x.iteritems()), key=lambda el: len(el[1]))
