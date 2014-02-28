#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p16.py
author: Zach Lamberty
created: 2014-02-16

Description:
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2*1000?

Notes:
    brute force? Python can do it!

"""


if __name__ == '__main__':

    print sum(int(el) for el in str(2**1000))
