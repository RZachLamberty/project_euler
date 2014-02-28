#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p34.py
author: Zach Lamberty
created: 2014-02-24

Description:
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Notes:
    For a number with N digits, the smallest value that can be made is 1. The
    largest is

        digits      high
        ------      -------
        2            725760
        3           1088640
        4           1451520
        5           1814400
        6           2177280
        7           2540160
        8           2903040

    The largest number we could possibly create is 2540160 (though that's not
    an answer, obviously)

"""

from scipy.misc import factorial


factorial = {str(i): factorial(i) for i in range(10)}


def facify(i):
    if i % 1000 == 0:
        print i
    return sum([factorial[el] for el in str(i)])


if __name__ == '__main__':
    x = [i for i in xrange(3, 2540161) if facify(i) == i]
    print x
    print sum(x)
