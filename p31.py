#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p31.py
author: Zach Lamberty
created: 2014-02-23

Description:
    In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?

Notes:
    brute force with generators, why anything else??

"""

from itertools import product


COINS = (1, 2, 5, 10, 20, 50, 100, 200)


if __name__ == '__main__':

    x = {(target, 0): 1 for target in range(200 + 1)}

    for target in range(200 + 1):
        for i in range(1, len(COINS)):
            coin = COINS[i]
            x[target, i] = x[target, i - 1]
            x[target, i] += x[target - coin, i] if target >= coin else 0

    print x[200, 7]
