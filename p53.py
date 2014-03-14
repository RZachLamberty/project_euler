#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p53.py
author: Zach Lamberty
created: 2014-03-13

Description:
    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general,

    nCr =      n!      , where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
            r!(n−r)!

    It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

    How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
    greater than one-million?

Notes:
    Yeah I'm just gonna cheat I think.

"""

import scipy.special


N = 1000000


if __name__ == '__main__':

    count = 0

    for n in range(1, 101):
        i = 0
        bigNuff = False
        while i < (n + 1.) / 2:
            if scipy.special.binom(n, i) > N:
                bigNuff = True
                break
            i += 1
        if bigNuff:
            count += (n + 1) - 2 * i

    print 'count = {}'.format(count)
