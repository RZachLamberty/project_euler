#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p43.py
author: Zach Lamberty
created: 2014-03-06

Description:
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up
    of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
    note the following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

Notes:
    Pretty easy with itertools. Only notable simplifications:

        first property ==> d4 is even
        third property ==> d6 = 0 or 5

    there are thus 10 * 8! possible choices

"""

from itertools import permutations


def sub_string_divisible_all(numStr):
    """ Given a number string, check the sub-string divisibility """
    return all(sub_string_divisible_piece(numStr, i, 3, val)
               for (i, val) in ((2, 3),
                                (4, 7),
                                (5, 11),
                                (6, 13),
                                (7, 17)))


def sub_string_divisible_piece(numStr, i, l, val):
    return int(numStr[i: i + l]) % val == 0


if __name__ == '__main__':

    s = set()

    evens = set([0, 2, 4, 6, 8])
    fives = set([0, 5])
    allnums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for d4 in evens:
        fivesNow = set(fives)
        fivesNow.discard(d4)
        for d6 in fivesNow:
            allnumsNow = set(allnums)
            allnumsNow.discard(d4)
            allnumsNow.discard(d6)
            for (d1, d2, d3, d5, d7, d8, d9, d10) in permutations(allnumsNow):
                n = '{}{}{}{}{}{}{}{}{}{}'.format(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
                if sub_string_divisible_all(n):
                    s.add(int(n))

    print s
    print sum(s)
