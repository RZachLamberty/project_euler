#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p45.py
author: Zach Lamberty
created: 2014-03-09

Description:
    Triangle, pentagonal, and hexagonal numbers are generated by the following
    formulae:

        Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
        Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
        Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...

    It can be verified that T285 = P165 = H143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.

Notes:
    First and foremost, there is a one to one mapping from Hex to Tri (not
    complet, however). Therefore we need only check certain triangle numbers:

        T_{2a - 1} = H_a ==> Only check T_n for n odd

    The goal, then, is to find the first post-285 n st T_n is equal to some
    pentagonal number. I think the fastest way to do this is to do a "ladder"
    update:
        if T_i == P_j:
            we win!!
        elif T_i < P_j:
            i += 1
        else:
            j += 1

    And so on.

"""

from projecteuler import triagonal, pentagonal, hexagonal


if __name__ == '__main__':

    i, j = 287, 165

    while True:
        Ti, Pj = triagonal(i), pentagonal(j)
        if Ti == Pj:
            break
        elif Ti > Pj:
            j += 1
        else:
            i += 2

    k = (i + 1) / 2
    Hk = hexagonal(k)
    print 'T_{} = {}'.format(i, Ti)
    print 'P_{} = {}'.format(j, Pj)
    print 'H_{} = {}'.format(k, Hk)