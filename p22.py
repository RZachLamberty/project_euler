#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p22.py
author: Zach Lamberty
created: 2014-02-16

Description:
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?

Notes:
    Should be easy.

"""

def name_val(name):
    return sum([ord(l) - 64 for l in name])


if __name__ == '__main__':

    with open('names.txt', 'rb') as fIn:
        s = sorted([el.replace('"', '') for el in fIn.read().split(',')])

    print sum((i + 1) * name_val(el) for (i, el) in enumerate(s))
