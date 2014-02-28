#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p25.py
author: Zach Lamberty
created: 2014-02-18

Description:
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?

Notes:
    Generator written and saved in projecteuler. Super easy deal.

    For large fib vals,

    F(n) = round(phi**n / sqrt(5))

    phi**n / sqrt(5)            >   10**999
    n * log(phi) - .5 * log(5)  >   999 * log(10)

"""

from math import log
from projecteuler import fibonacci


if __name__ == '__main__':

    # Generator way
    for (i, f) in enumerate(fibonacci()):
        if f / 10**999:
            break

    print 'the {}-th term is\n\n{}\n'.format(i + 1, f)

    # Math way
    phi = 1.6180
    n = (999. * log(10.) + .5 * log(5)) / log(phi)
    print 'By Great Maths we have i = {}'.format(n)
