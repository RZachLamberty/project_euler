#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p37.py
author: Zach Lamberty
created: 2014-02-27

Description:
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Notes:
    Get the primes as before. then just do some voodoo. Probably a smarter way
    but def not necessary.

"""

from projecteuler import is_prime


def is_trunc(p, primes):
    return left_trunc(p, primes) and right_trunc(p, primes)


def left_trunc(p, primes):
    s = str(p)
    return all(is_prime(int(s[i:]), primes, onePrime=False) for i in range(1, len(s)))


def right_trunc(p, primes):
    s = str(p)
    return all(is_prime(int(s[:i]), primes, onePrime=False) for i in range(1, len(s)))


if __name__ == '__main__':

    primes = {}
    p = 2
    truncPrimes = set()

    while len(truncPrimes) < 11:
        if p > 7 and is_prime(p, primes, onePrime=False) and is_trunc(p, primes):
            print 'Adding p = {}'.format(p)
            truncPrimes.add(p)
        p += 1

    print 'Truncatable primes: {}'.format(truncPrimes)
    print 'Sum: {}'.format(sum(truncPrimes))
