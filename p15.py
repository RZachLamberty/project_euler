#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p15.py
author: Zach Lamberty
created: 2014-02-16

Description:
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

    < https://projecteuler.net/project/images/p_015.gif >

    How many such routes are there through a 20×20 grid?

Notes:
    So easy! It's equivalent to the number of 2N-length binary numbers which
    have N 0s and N 1s -- i.e. binomial(2N, N)

"""

from scipy.special import binom

if __name__ == '__main__':

    print binom(40, 20)
