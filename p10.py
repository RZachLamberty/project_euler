#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p10.py
author: Zach Lamberty
created: 2014-02-13

Description:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

Notes:
    Gonna use the same process as before with catching all primes by checking
    divisibility

"""

import collections

PMAX = 2000000

if __name__ == '__main__':

    marked = collections.defaultdict(int)

    value = 3
    s = 2
    while value < PMAX:
        if not marked[value]:
            s += value
            i = value
            while i < PMAX:
                marked[i] = 1
                i += value
        value += 2

    print s
