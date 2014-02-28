#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p35.py
author: Zach Lamberty
created: 2014-02-24

Description:
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100:

        2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

Notes:
    Get all the primes (projecteuler) under one million, and go through that
    (doing the permutations, etc).

    Can't have an even number in it!

"""

from projecteuler import all_primes_between


def perms(p):
    s = set()
    sp = str(p)
    L = len(sp)
    s = {int(''.join([sp[(offset + j) % L] for j in range(L)]))
         for offset in range(L)}

    return s


def any_evens(p):
    return any(int(el) % 2 == 0 for el in str(p)) or p == 2


if __name__ == '__main__':

    n = all_primes_between(2, 1000000)
    unchecked = set(n)

    circularPrimes = set()

    i = 0
    for p in n:
        if any_evens(p):
            unchecked.discard(p)
        else:
            if p / 1000 > i:
                print p
                i = p / 1000
            if p in unchecked:
                ps = perms(p)
                isCircular = all(el in n for el in ps)
                for el in ps:
                    unchecked.discard(el)
                if isCircular:
                    circularPrimes.update(ps)

    print circularPrimes
    print len(circularPrimes)
