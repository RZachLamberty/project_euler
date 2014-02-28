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


#---------------------------#
#   Divisors and Factors    #
#---------------------------#

def divisors_list(n):
    """ Retrun a dictionary containing all the divisors of all numbers up to n

    """
    d = defaultdict(set)
    for i in range(1, n / 2 + 1):
        d[i].add(1)
        for j in range(2, n / i + 1):
            d[i * j].add(i)

    return d


#---------------------------#
#   Prime numbers           #
#---------------------------#

def is_prime(n, hashDic=None, onePrime=True):
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
