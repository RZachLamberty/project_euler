#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p46.py
author: Zach Lamberty
created: 2014-03-09

Description:
    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

        9 = 7 + 2×12
        15 = 7 + 2×22
        21 = 3 + 2×32
        25 = 7 + 2×32
        27 = 19 + 2×22
        33 = 31 + 2×12

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?

Notes:
    For every odd number o, check if it is prime (if so, pass). If not prime,
    for every prime less than it, check if the difference is twice a square. Do
    this until no such doulbe square is found. Voila.

"""

from math import sqrt
from projecteuler import is_prime


def goldbach_was_right(o, p):
    """ See if the differnce between o and p is twice a square """
    x = sqrt((o - p) / 2.)
    return x == int(x)


if __name__ == '__main__':

    primes = {1, 2}

    o = 3
    while True:
        if is_prime(o):
            primes.add(o)
        else:
            if any([goldbach_was_right(o, p) for p in primes]):
                pass
            else:
                break
        # Only odds
        o += 2

    print o
