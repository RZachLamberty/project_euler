#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p33.py
author: Zach Lamberty
created: 2014-02-24

Description:
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.

Notes:
    10i + j     i or j
    -------  =  ------
    10k + l     k or l

    This yields the following (non-trivial) possibilities:

    i = k:
        Only trivial solutions (5i / 5i, e.g.)
    i = l:
        10ik + jk = 10jk + ij
        10ik - 9jk - ij = 0
    j = k:
        10il + lk = 10ik + il
        10ik - 9il - kl = 0 (same as above, but after (kijl) )

"""


def frac(i, j, k, l):
    return (10. * i + j) / (10. * k + l)


def yep(i, j, k, l):
    if i == l:
        return frac(i, j, k, l) == float(j) / k
    if j == k:
        return frac(i, j, k, l) == float(i) / l
    return False


if __name__ == '__main__':
    x = set()
    for a in range(10, 100):
        sa = str(a)
        if '0' not in sa:
            i, j = [int(el) for el in sa]
            for b in range(a + 1, 100):
                sb = str(b)
                if '0' not in sb:
                    k, l = [int(el) for el in sb]
                    if yep(i, j, k, l):
                        x.add((i, j, k, l))
    p = 1.
    for (i, j, k, l) in x:
        p *= frac(i, j, k, l)

    print p
