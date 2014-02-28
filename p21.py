#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p21.py
author: Zach Lamberty
created: 2014-02-16

Description:
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are

        1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.

    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

Notes:


"""

from collections import defaultdict
from math import sqrt


MAX_NUM = 10000


def divisors_list(n):
    """ Retrun the sum of all the divisors of all numbers up to n """
    d = defaultdict(set)
    for i in range(1, n / 2 + 1):
        d[i].add(1)
        for j in range(2, n / i):
            d[i * j].add(i)

    #return d
    return {k: sum(v) for (k, v) in d.iteritems()}


if __name__ == '__main__':

    d = divisors_list(MAX_NUM)

    print sum(a for a in d if d[a] != a and d[a] < MAX_NUM and d[d[a]] == a)
