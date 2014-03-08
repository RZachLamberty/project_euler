#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p41.py
author: Zach Lamberty
created: 2014-03-05

Description:
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?

Notes:
    Upper bound is 987654321. Let's just brute force it with itertools

    Update -- upper bound is actually 7654321!
        8 numbers will be divisible by 3, and hence so will 9. Awesome

"""

from itertools import permutations

from projecteuler import is_prime


if __name__ == '__main__':

    pMax = 1

    for i in range(2, 8):
        for p in permutations(range(1, i + 1)):
            p = int(''.join([str(el) for el in p]))
            if is_prime(p):
                pMax = max(p, pMax)

    print "pMax = {}".format(pMax)
