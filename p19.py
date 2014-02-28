#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
module: p19.py
author: Zach Lamberty
created: 2014-02-16

Description:
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

Notes:
    With datetime this is trivial; I'll solve it the "pure" way instead.

"""

import datetime


JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(1, 13)
SUN, MON, TUE, WED, THU, FRI, SAT = range(7)


def is_leap_year(y):
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))


def daily_grind():
    c, y, m, d = 19, 1900, JAN, 1
    wd = MON
    yield c, y, m, d, wd
    while (y, m, d) < (2001, JAN, 1):
        # Weekdays are easy
        wd += 1
        wd %= 7

        # most days are easy
        if 1 <= d < 28:
            d += 1
        # Leap year stuff
        elif d == 28:
            if m == FEB and not is_leap_year(y):
                m, d = MAR, 1
            else:
                d += 1
        # more leap year stuff
        elif d == 29:
            if m == FEB:
                m, d = MAR, 1
            else:
                d += 1
        # 30 day months
        elif d == 30:
            if m in [SEP, APR, JUN, NOV]:
                m += 1
                d = 1
            else:
                d += 1
        # The rest and turns of centuries / years
        elif d == 31:
            # Happy new year!
            if m == DEC:
                m, d = JAN, 1
                if y % 100 == 0:
                    c += 1
                y += 1
            else:
                m += 1
                d = 1
        else:
            raise ValueError("something went wrong: {} {} {} {}".format(c, y, m, d))

        yield c, y, m, d, wd


if __name__ == '__main__':

    print 'my guess: {}'.format(sum(c == 20 and d == 1 and wd == SUN
                                    for (c, y, m, d, wd) in daily_grind()))

    c = 0
    d = datetime.date(1901, 1, 1)
    while d < datetime.date(2001, 1, 1):
        if d.weekday() == 6 and d.day == 1:
            c += 1
        d += datetime.timedelta(1)

    print 'The good way {}'.format(c)
