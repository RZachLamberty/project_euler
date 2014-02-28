#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p4.py
author: Zach Lamberty
created: 2014-02-13

Description:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    https://projecteuler.net/problem=4

    "ijk" = 100i + 10j + k
    "ijk" * "lmn" = (100i + 10j + k) * (100l + 10m + n)
                  = 10000il + 1000im + 100in + 1000jl + 100jm + 10jn + 100kl + 10km + kn
                  =  10,000 (il)
                    + 1,000 (im + jl)
                    +   100 (in + jm + kl)
                    +    10 (jn + km)
                    +     1 (kn)

    Scratch all this. Just convert it to a string, silly.

"""

#import argparse

from itertools import product


if __name__ == '__main__':

    #parser = argparse.ArgumentParser()
    #parser.add_argument("-n", "--maxnum", type=int)
    #
    #args = parser.parse_args()

    maxnum = 1000

    #f = (el for el in product(range(10), repeat=6) if filter(i, j, k, l, m, n))
    m = 0
    for (a, b) in product(range(maxnum), repeat=2):
        p = a * b
        s = str(p)
        m = max(m, p) if s == s[::-1] else m

    print m
