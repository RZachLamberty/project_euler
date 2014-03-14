#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p51.py
author: Zach Lamberty
created: 2014-03-13

Description:
    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family:

        56003, 56113, 56333, 56443, 56663, 56773, and 56993.

    Consequently 56003, being the first member of this family, is the smallest
    prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight prime
    value family.

Notes:
    prime number generator... Then I guess we will just check each one? no good
    idea here.

"""

from itertools import combinations
from projecteuler import primes, is_prime


CHOOSE = {}
PRIME_DIC = {}


def eight_primes(sp, i):
    """ Replace every set of i characters from sp and check if it is prime """
    l = len(sp)
    for iSet in choose(l, i):
        notPrimes = 0
        for r in replacements(sp, iSet):
            if (len(str(r)) != len(sp)) or (not is_prime(r, PRIME_DIC)):
                notPrimes += 1
            if notPrimes == 3:
                break
        if notPrimes < 3:
            return True, iSet

    return False, None


def choose(l, i):
    """ doc """
    try:
        return CHOOSE[l, i]
    except:
        x = [s for s in combinations(range(l), i)]
        CHOOSE[l, i] = x
        return x


def replacements(sp, iSet):
    for a in range(10):
        yield int(''.join([str(a) if i in iSet else el
                           for (i, el) in enumerate(sp)]))


if __name__ == '__main__':

    for p in primes():
        if p % 1000 < 3:
            print p
        sp = str(p)
        l = len(sp)
        areEightPrimes = False
        for i in range(1, l):
            (areEightPrimes, iSet) = eight_primes(sp, i)
            if areEightPrimes:
                print 'p    = {}'.format(p)
                print 'iSet = {}'.format(iSet)
                for r in replacements(sp, iSet):
                    print '\tr = {}'.format(r)
                    print '\tis_prime(r) = {}'.format(is_prime(r))
                break
        if areEightPrimes:
            break
