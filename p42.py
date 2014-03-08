#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p42.py
author: Zach Lamberty
created: 2014-03-05

Description:
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
    so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, how many are triangle
    words?

Notes:
    Pretty straightforward at first. Pre-assemble a dictionary to do the letter
    value lookup, count the number of triangle words, etc.

"""

from collections import defaultdict


LETTER_VAL = {el: i + 1 for (i, el) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}


def word_val(word):
    return sum(LETTER_VAL[el] for el in word)


def triangle_numbers(tMax):
    """ Return a list of all triangle numbers less than some max value tMax """
    return [n * (n + 1) / 2 for n in range(1, tMax + 1)]


if __name__ == '__main__':

    with open('words.txt', 'rb') as fIn:
        words = fIn.read().replace('"', '').split(',')

    wordVals = defaultdict(int)
    for word in words:
        wordVals[word_val(word)] += 1

    count = sum(n for (wordVal, n) in wordVals.iteritems()
                if wordVal in triangle_numbers(max(wordVals)))

    print count
