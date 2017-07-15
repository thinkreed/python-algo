#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/7'

"""


class Solution:
    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)


if __name__ == '__main__':
    print(Solution().reverse(-123))
