#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p23.py
author: Zach Lamberty
created: 2014-02-16

Description:
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.

Notes:
    <notes>

"""

import itertools

import projecteuler


NMAX = 28123


if __name__ == '__main__':

    # Get the sum of all divisors
    d = {k for (k, v) in projecteuler.divisors_list(NMAX).iteritems()
         if k < sum(v)}

    marked = [0] * NMAX

    for (e1, e2) in itertools.product(d, repeat=2):
        if e1 + e2 < NMAX:
            marked[e1 + e2] = 1

    print sum(i for (i, el) in enumerate(marked) if el == 0)
