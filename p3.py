#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: Problem 3
author: Zach Lamberty
created: 2014-02-13

Description:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i: : 2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


if __name__ == '__main__':

    #NUM = 600851475143
    NUM = 600851475143
    for p in reversed(primes(int(NUM**.5))):
        if not NUM % p:
            print p
            break
