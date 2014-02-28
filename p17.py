#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p17.py
author: Zach Lamberty
created: 2014-02-16

Description:
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.

Notes:
    No easy way to do this one -- just have to write out all the number words

"""

ONES = {
    0: 0,
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),
}

TEENS = {
    0: len('ten'),
    1: len('eleven'),
    2: len('twelve'),
    3: len('thirteen'),
    4: len('fourteen'),
    5: len('fifteen'),
    6: len('sixteen'),
    7: len('seventeen'),
    8: len('eighteen'),
    9: len('nineteen'),
}

TENS = {
    2: len('twenty'),
    3: len('thirty'),
    4: len('forty'),
    5: len('fifty'),
    6: len('sixty'),
    7: len('seventy'),
    8: len('eighty'),
    9: len('ninety'),
}


def num_str_len(n):
    i, j, k, l = [int(el) for el in str(n).zfill(4)]

    if i == 1:
        return len('onethousand')
    else:
        nsl = 0

        # hundreds
        nsl += ONES[j] + (len('hundredand') if j else 0)

        # Teens and ones
        if k == 0:
            # Add the integer or kill the "and" for 00
            nsl += ONES[l] if l else -3
        elif k == 1:
            nsl += TEENS[l]
        else:
            nsl += TENS[k]
            nsl += ONES[l] if l else 0

    return nsl


if __name__ == '__main__':

    print sum(num_str_len(n) for n in range(1, 1001))
