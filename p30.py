#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p30.py
author: Zach Lamberty
created: 2014-02-22

Description:
    Surprisingly there are only three numbers that can be written as the sum of
    fourth powers of their digits:

        1634 = 1**4 + 6**4 + 3**4 + 4**4
        8208 = 8**4 + 2**4 + 0**4 + 8**4
        9474 = 9**4 + 4**4 + 7**4 + 4**4

    As 1 = 1**4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.

Notes:
    There needs to be a highest possible number or this problem doesn't make
    sense. The largest n-digit number we can have is n 9's.

        n * 9**5 = n * 59049

    for n = 7 we get 413343, a 6 digit number -- we can't get to any 7 digit
    number. We can stop at the largest 6-digit number available,

        6 * 9**5 = 354294

"""

if __name__ == '__main__':

    x = [i for i in range(2, 354295) if i == sum(int(el)**5 for el in str(i))]

    print x
    print sum(x)
