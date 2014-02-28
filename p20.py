#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p20.py
author: Zach Lamberty
created: 2014-02-16

Description:
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example,

        10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,

    and the sum of the digits in the number 10! is

        3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

Notes:
    brute force, but I'll program the fact for fun

"""

N = 100


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


if __name__ == '__main__':

    print sum([int(el) for el in str(factorial(N))])
