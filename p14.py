#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p14.py
author: Zach Lamberty
created: 2014-02-16

Description:
    The following iterative sequence is defined for the set of positive
    integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

Notes:
    <notes>

"""

N = 1000000


def collatz_step(n):
    return 3 * n + 1 if n % 2 else n / 2


if __name__ == '__main__':

    marked = [0] * N

    i = 2
    maxLen = 0
    maxI = 2

    while i < N:
        if not marked[i]:
            c = i
            l = 0
            print i
            while c != 1:
                if c < N:
                    marked[c] = 1
                c = collatz_step(c)
                l += 1
            (maxLen, maxI) = (maxLen, maxI) if maxLen > l else (l, i)
        i += 1

    print 'collatz chain for i = {}:\nlen = {}'.format(maxI, maxLen)
