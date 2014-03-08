#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p38.py
author: Zach Lamberty
created: 2014-02-27

Description:
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?

Notes:
    is there any good way to do this?

    First, note: for a given A and range (1, ..., n), we have a final product
    of

        (A * n) + (A * (n - 1)) * 10**("length of (A * n)") + ...

    So there is a naiv-ish way to reconstruct this. How can we calculate that
    "length of ..." part? len(str(A * n))

    The easy / naive way is just this:

        digit length    max n
        ------------    -----
        1               9
        2               5
        3               3
        4               2

    I can wrap this in a better generator, or just make that the function

"""


def mult_cat(a, n):
    return ''.join([str(a * i) for i in range(1, n + 1)])


def is_pandigital(pd):
    return ''.join(sorted(pd)) == '123456789'


if __name__ == '__main__':

    a, n = 1, 1

    pandigitals = set()

    mc = mult_cat(a, n)
    while len(str(a)) < 5:
        print a
        while len(mc) <= 9:
            n += 1
            mc = mult_cat(a, n)
            if is_pandigital(mc):
                pandigitals.add((a, n, mc))
        n = 1
        a += 1
        mc = mult_cat(a, n)

    print pandigitals
    print max(pandigitals, key=lambda x: int(x[2]))
