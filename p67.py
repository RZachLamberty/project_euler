#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p67.py
author: Zach Lamberty
created: 2014-02-13

Description:
    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with a
    triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)

Notes:
    Let's think about bottom-up. Replace each point in row N-1 with the sum of
    that value and the max of its two choices in row N. This will ensure we end
    with the largest possible value!

"""


def load_triangle(tName):
    with open(tName, 'rb') as fIn:
        T = [[int(el) for el in row.split(' ')] for row in fIn]
    return T


def update_val(T, i, j):
    return T[i][j] + max(T[i + 1][j], T[i + 1][j + 1])


if __name__ == '__main__':

    T = load_triangle('triangle.txt')

    for i in range(len(T) - 2, -1, -1):
        for j in range(len(T[i])):
            T[i][j] = update_val(T, i, j)

    print T[0][0]
