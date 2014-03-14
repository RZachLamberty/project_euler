#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p48.py
author: Zach Lamberty
created: 2014-03-10

Description:
    The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

    Find the last ten digits of the series,
    1**1 + 2**2 + 3**3 + ... + 1000**1000.

Notes:
    just continually mod everything by 10**N; multiplication by numbers beyond
    that can't affect the overall

"""

A = 1000
N = 10
NN = 10**N

if __name__ == '__main__':
    x = 0
    for a in range(1, A + 1):
        print "a = {}".format(a)
        xNow = 1
        for i in range(a):
            xNow *= a
            xNow %= NN
        x += xNow
        x %= NN

    print "x = {}".format(x)
