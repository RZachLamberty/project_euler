#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: Problem 1
author: Zach Lamberty
created: 2014-02-13

Description:
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == '__main__':

    threes = sum(3 * (i + 1) for i in range(999/3))
    fives = sum(5 * (i + 1) for i in range(999/5))
    fifteens = sum(15 * (i + 1) for i in range(1000/15))

    print threes + fives - fifteens
