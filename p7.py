#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p7.py
author: Zach Lamberty
created: 2014-02-13

Description:
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10,001st prime number?

"""

from math import sqrt

PRIMES = 10001

if __name__ == '__main__':

    primes = {2}

    n = 3
    while len(primes) < PRIMES:
        # check if the number is divisible by any previous prime
        if any(not n % p for p in (el for el in primes if el <= sqrt(n))):
            pass
        else:
            primes.add(n)

        n += 2

    print n - 2

