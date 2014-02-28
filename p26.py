#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p26.py
author: Zach Lamberty
created: 2014-02-20

Description:
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

        1/2 =   0.5
        1/3 =   0.(3)
        1/4 =   0.25
        1/5 =   0.2
        1/6 =   0.1(6)
        1/7 =   0.(142857)
        1/8 =   0.125
        1/9 =   0.(1)
        1/10    =   0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

Notes:
    What makes 1 / 7 so long?

    1 / d = 1.0000000000000000 / 7

    1 / 7       = 0 r 1
    10 / 7      = 1 r 3
    30 / 7      = 4 r 2
    20 / 7      = 2 r 6
    60 / 7      = 8 r 4
    40 / 7      = 5 r 5
    50 / 7      = 7 r 1

    So pretty straight forward. I'll solve this by creating a map of one digit
    to the next. Note that for larger d we won't always get a single digit
    remainder:

    d = 42

    1 / 42      = 0 r 1
    10 / 42     = 0 r 10
    100 / 42    = 2 r 16
    160 / 42    = 3 r 34
    340 / 42    = 8 r 4
    40 / 42     = 0 r 40
    400 / 42    = 9 r 22
    220 / 42    = 5 r 10
    100 / 42    = 2 r 16
    ...

    So it's the *remainders* that matter.

"""


def remainder_map(d):
    rems = {}

    n = 1
    p, r = n / d, n % d
    while True:
        n = r * 10
        p, r, rLast = n / d, n % d, r

        if rLast in rems:
            break
        else:
            rems[rLast] = r

    return rems


def chain_length(rems):
    return len(rems)


if __name__ == '__main__':

    print max((d for d in range(2, 1000)),
              key=lambda x: chain_length(remainder_map(x)))
