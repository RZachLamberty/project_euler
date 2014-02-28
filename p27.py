#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p27.py
author: Zach Lamberty
created: 2014-02-20

Description:
    Euler discovered the remarkable quadratic formula:

        n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40

        40**2 + 40 + 41 = 40(40 + 1) + 41

    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.

    The incredible formula  n² − 79n + 1601 was discovered, which produces 80
    primes for the consecutive values n = 0 to 79. The product of the
    coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |−4| = 4)

    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n = 0.

Notes:
    We will hash our primes to make lookup more effective... should also add
    a quick "is prime" function to projecteuler... done.

"""

from functools import partial
from itertools import product

from projecteuler import is_prime


def quad(x, a, b):
    return x * (x + a) + b


def quad_now(a, b):
    return partial(quad, a=a, b=b)


def num_consec_primes(qab, isPrime):
    l, n = 0, 0
    while is_prime(qab(n), hashDic=isPrime):
        l += 1
        n += 1

    return l


if __name__ == '__main__':

    isPrime = {}
    lMax, aMax, bMax = 0, None, None

    for (a, b) in product(range(-999, 1000), repeat=2):
        if a % 100 == 0 and b % 100 == 0:
            print '(a, b) = ({}, {})'.format(a, b)
        l = num_consec_primes(quad_now(a, b), isPrime)
        if l > lMax:
            lMax, aMax, bMax = l, a, b

    print """n**2 + {a:} * n + {b:}
(a = {a:}, b = {b:})
results in {l:} consecutive primes.

a * b = {ab:}""".format(a=aMax, b=bMax, l=lMax, ab=aMax * bMax)
