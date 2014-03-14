#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p49.py
author: Zach Lamberty
created: 2014-03-10

Description:
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit increasing
    sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

Notes:
    Brute force with my primes generator should be good enough. If we happen
    to get some primes which do have permutations (but not three) we can boot
    em.

"""

from itertools import permutations
from projecteuler import all_primes_between


if __name__ == '__main__':

    primes = all_primes_between(2, 9999)

    x = []
    for p in primes:
        if p < 1000:
            pass
        else:
            for p2 in permutations(str(p)):
                p2 = int(''.join(p2))
                if (p2 > p) and (p2 in primes):
                    p3 = 2 * p2 - p
                    if (p3 < 10000) and (p3 in primes) and (sorted(str(p3)) == sorted(str(p))):
                        x.append((p, p2, p3))

    print x
