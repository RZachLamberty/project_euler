#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p24.py
author: Zach Lamberty
created: 2014-02-16

Description:
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits

        0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Notes:
    the smallest few:

        01234567 89
        01234567 98

        0123456 879
        0123456 897
        0123456 978
        0123456 987

        012345 7689
        012345 7698
        012345 7869
        012345 7896
        012345 7968
        012345 7986
        012345 8679
        012345 8697
        012345 8769
        012345 8796
        012345 8967
        012345 8976
        012345 9678
        012345 9687
        012345 9768
        012345 9786
        012345 9867
        012345 9876

    SO. The first 2! = 2 numbers are the ordered permutations of (8, 9). The
    first 3! = 6 are the ordered permutations of (7, 8, 9). The first... etc

    9! = 362880, so the number must be between 2 000 000 000 and 3 000 000 000

    That is, the first number is 2.

    8! = 40320... this can continue from here recursively to find the best
    possible number!

    the formula for the order of number abcdefghij is

        a * factorial(10)   0
      + b * factorial(9)    2
      + c * factorial(8)    6
      + d * factorial(7)    5
      + e * factorial(6)
      + f * factorial(5)
      + g * factorial(4)
      + h * factorial(3)
      + i * factorial(2)
      + j * factorial(1)

    Find the one for which that sum is 1,000,000

"""

import itertools

from scipy.misc import factorial


def num_perm_n_less_than(elSet, maxVal):
    for (i, el) in enumerate(elSet):
        if el * factorial(len(elSet)) >= maxVal:
            break
    return i - 1


if __name__ == '__main__':

    # All choices, and the total desired number
    numbers = range(10)
    tot = 1000000
    tot = 999999

    perm = []
    while numbers:
        i = num_perm_n_less_than(numbers, tot)
        p = numbers.pop(num_perm_n_less_than(numbers, tot))
        tot -= i * factorial(len(numbers))
        perm.append(p)

    print ''.join([str(el) for el in perm])

    i = 0
    for p in itertools.permutations(range(10), 10):
        i += 1
        if i == 1000000:
            break

    print p
