#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p28.py
author: Zach Lamberty
created: 2014-02-22

Description:
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?

Notes:
    Can possibly be done recursively.

    3 x 3: 25

    Top right corner is 9; we get
        9 + 4
        9 + 4 + 4
        9 + 4 + 4 + 4, and
        9 + 4 + 4 + 4 + 4

    Let P(1) = 1
        P(3) = 1 + (1 + 2) + (1 + 2 + 2) + (1 + 2 + 2 + 2) + (1 + 2 + 2 + 2 + 2)
             = 1 + 4 * 1 + 10 * (3 - 1)
             = 1 + 4 * 1**2 + 10 * (3 - 1)
        P(5) = 25 + 9 * 3**2 + 10 * (5 - 1)
        ...

    Generally speaking, then,

        P(2n + 1) = P(2n - 1) + 4 * (2n - 1)**2 + 10 * (2n)

"""


def P(i):
    if i % 2:
        return 1 if i == 1 else P(i - 2) + 4 * (i - 2)**2 + 10 * (i - 1)
    else:
        raise ValueError("Only defined for even i")


if __name__ == '__main__':

    print P(1001)
