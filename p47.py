#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p47.py
author: Zach Lamberty
created: 2014-03-09

Description:
    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors
    are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

Notes:
    First, start at 210 -- it's the first number with four distinct prime
    factors.

    Next, I will just iterate through and count consecutives.

    Also, start at 210. It's the first number with four distinct prime factors

"""

import argparse

from projecteuler import prime_factorization_opt


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("magic_number", default=4, type=int, help="Number of factors")
    args = parser.parse_args()

    count = 0
    n = 0
    while not count >= args.magic_number:
        if n % 1000 == 0:
            print n
        n += 1
        pf = prime_factorization_opt(n, 1000000)
        if len(pf) == args.magic_number:
            count += 1
        else:
            count = 0

    print range(n - args.magic_number + 1, n + 1)
