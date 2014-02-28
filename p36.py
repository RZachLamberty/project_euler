#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p36.py
author: Zach Lamberty
created: 2014-02-27

Description:
    The decimal number, 585 = 10010010012 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)

Notes:
    There are fewer palindromic decimal nubmers than binary numbers, so only
    grab them.

    Also, no leading zeros in base 2 ==> ends in 1 ==> is odd ==> only starts
    with odd numbers.

"""


def decimal_palindromes(N):
    """ Generator for decimal palindromes """
    i = 1
    while i < N:
        s = str(i)
        if s == s[::-1]:
            yield i

        # Ensure it stays odd
        i += 2


def is_bin_palindrome(i):
    b = str(bin(i))[2:]
    return b == b[::-1]


if __name__ == '__main__':

    print sum(dp for dp in decimal_palindromes(1E6) if is_bin_palindrome(dp))
