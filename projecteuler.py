#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: projecteuler.py
author: Zach Lamberty
created: 2014-02-16

Description:
    Some things keep poppin up -- here's a module to collect them!

Usage:
    <usage>

"""

from collections import defaultdict
from math import sqrt


#---------------------------#
#   Common Generators       #
#---------------------------#

def fibonacci():
    """ generator for the finonacci sequence """
    a, b = 1, 0
    while True:
        yield a
        a, b = a + b, a


def primes(oneIsPrime=False, maskSize=100000):
    """ Should be pretty simple if we keep a global list """
    primeSet = set()
    marked = defaultdict(int)

    if oneIsPrime:
        primeSet.add(1)
        yield 1
    else:
        primeSet.add(2)
        yield 2

    p = 3
    while p < maskSize:
        if not marked[p]:
            primeSet.add(p)
            _update_mask(p, marked, maskSize)
            yield p
        p += 2

    # We've reached the top of our mask. From here on out just increment by 2
    # and check if any of the previous primeSet divide it
    while True:
        if any(p % i == 0 for i in primeSet):
            pass
        else:
            primeSet.add(p)
            yield p
        p += 2


def _update_mask(p, marked, maskSize=100000):
    ip = p
    while ip < maskSize:
        marked[ip] = True
        ip += 2 * p


#---------------------------#
#   Divisors and Factors    #
#---------------------------#

def divisors_list(n):
    """ Return a dictionary containing all the divisors of all numbers up to n

    """
    d = defaultdict(set)
    for i in range(1, n / 2 + 1):
        d[i].add(1)
        for j in range(2, n / i + 1):
            d[i * j].add(i)

    return d


def prime_factorization(n):
    """ Return the prime factorization of n as a dictionary """
    divisors = {}
    p = 2

    # 2s first
    while n % 2 == 0:
        if 2 not in divisors:
            divisors[p] = 0
        divisors[p] += 1
        n /= p

    # now odds
    p = 3
    while n != 1:
        while n % p == 0:
            if p not in divisors:
                divisors[p] = 0
            divisors[p] += 1
            n /= p
        p += 2

    return divisors


_primeset = ()


def prime_factorization_2(n):
    """ Return the prime factorization of n as a dictionary """
    global _primeset
    print _primeset
    divisors = {}

    primegen = primes()

    i = 0
    while n != 1:
        try:
            p = _primeset[i]
        except:
            p = primegen.next()
            _primeset += (p,)

        while n % p == 0:
            if p not in divisors:
                divisors[p] = 0
            divisors[p] += 1
            n /= p

        i += 1

    return divisors


def prime_factorization_opt(n, nMax=100000):
    """ Pre-load a set of primes, then do the same as the "original" """
    global _primeset

    if not _primeset:
        _primeset = all_primes_between(2, nMax)

    divisors = {}

    i = 0
    while n != 1:
        p = _primeset[i]
        while n % p == 0:
            if p not in divisors:
                divisors[p] = 0
            divisors[p] += 1
            n /= p
        i += 1

    return divisors


#---------------------------#
#   Prime numbers           #
#---------------------------#

def is_prime(n, hashDic=None, onePrime=False):
    basePrimes = [1, 2] if onePrime else [2]

    ip = (n > 0) and ((n in basePrimes)
                      or
                      ((n > 2)
                       and not
                       any(n % i == 0 for i in range(2, int(sqrt(n)) + 1))))

    if hashDic is not None:
        try:
            return hashDic[n]
        except:
            hashDic[n] = ip
            return ip
    else:
        return ip


def all_primes_between(l, h):
    """ Return a list of all the primes between l and h """
    marked = defaultdict(int)

    testVal = 2
    while testVal < h:
        if not marked[testVal]:
            for i in range(2, h / testVal + 1):
                marked[i * testVal] = 1
        testVal += 1

    return [p for (p, v) in marked.iteritems() if p >= l and not v]


#---------------------------#
#   N-agonal numbers        #
#---------------------------#

def triagonal(i):
    return i * (i + 1) / 2


def pentagonal(i):
    return i * (3 * i - 1) / 2


def hexagonal(i):
    return i * (2 * i - 1)


def n_agonal(N):
    return lambda x: (1 - N / 2) * x**2 + (2 - N / 2) * x
