#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p40.py
author: Zach Lamberty
created: 2014-03-05

Description:
    An irrational decimal fraction is created by concatenating the positive
    integers:

        0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

        d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

Notes:
    Brute force, basically. I can do it by hand, too. I did it that way by
    paper. I'll do it by hand, too :).

    Basic principle: given d_i and x_alpha < i < x_{alpha + 1}, there exists an
    n (a number with alpha digits) such that

        i is in [s_alpha + alpha * n + j for j in range(0, alpha)]

    and

        d_i = the jth integer in n (given j is the integer yielding equality)

    So find n and j, then get the jth number in n. Easy peasy.

    turning it around by rangifying it:

        s_alpha + alpha * n     <=  i                       < s_alpha + alpha * n + alpha = s_alpha + alpha * (n + 1)
        n                       <=  (i - s_alpha) / alpha   < n + 1

    find that n!

"""

from scipy import prod


def set_size(alpha):
    return alpha * 9 * 10**(alpha - 1)


def max_integer_set(N):
    x = [0]
    for i in range(1, N + 1):
        x.append(x[-1] + set_size(i))
    return x


INT_SET = max_integer_set(7)


def find_el_at(i):
    """ Find the number being printed in the vacinity of i, and then the exact
        number in that slot

    """
    if 0 < i < 10:
        return i

    alpha = max(a + 1 for (a, el) in enumerate(INT_SET) if i >= el)

    n = (i - INT_SET[alpha - 1] - 1) / alpha
    sn = str(n + 10**(alpha - 1)).zfill(alpha)
    for j, snj in enumerate(sn):
        if alpha * n + INT_SET[alpha - 1] + 1 + j == i:
            return int(snj)

    raise ValueError("Should have calculated element at d_i by now")


if __name__ == '__main__':

    toCatch = [1, 10, 100, 1000, 10000, 100000, 1000000]

    # By hand
    print "*** The Smart Way ***"
    x = {find_el_at(i) for i in toCatch}
    print x
    print prod([el for el in x])

    # Brute Force
    print "*** The Brute Force Way ***"
    i, n = 1, 1
    caught = []
    while toCatch:
        for a in [int(el) for el in str(n)]:
            if i in toCatch:
                toCatch.remove(i)
                caught.append((i, a))
            i += 1
        n += 1

    print caught

    print prod([el[1] for el in caught])
