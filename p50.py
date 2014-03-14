#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p50.py
author: Zach Lamberty
created: 2014-03-11

Description:
    The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?

Notes:
    Simple enough. Generate a list of primes, check the sum of all the sub-sets
    of increasing size. To do this, we make a cumulative sum. Then we check the
    offsets (csPrimes - csPrimes[i]) for the largest prime.

"""

from projecteuler import all_primes_between


N = 1000000
#N = 100


if __name__ == '__main__':

    primes = all_primes_between(2, N)
    primeSums = [0]
    for i in range(len(primes)):
        primeSums.append(primeSums[-1] + primes[i])

    L = len(primeSums)

    numberOfPrimes = 0
    pMax = 0
    for i in range(len(primeSums)):
        for j in range(i - numberOfPrimes - 1, -1, -1):
            dp = primeSums[i] - primeSums[j]
            if dp > N:
                break
            if dp in primes:
                numberOfPrimes = i - j
                pTop = primes[i]
                pMax = dp

    print 'number of primes = {}'.format(numberOfPrimes)
    print 'pTop             = {}'.format(pTop)
    print 'pMax             = {}'.format(pMax)
