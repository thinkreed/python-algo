#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/8'

"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        s = list(str.strip())

        flag = -1 if s[0] == '-' else 1

        if s[0] in ['+', '-']:
            del s[0]

        result = 0

        for i, digit in enumerate(s):
            if digit.isdigit():
                cur = result * 10 + (ord(digit) - ord('0'))
                result = cur
            elif i == 0:
                return 0
            else:
                return max(-2 ** 31, min(2 ** 31 - 1, result * flag))

        return max(-2 ** 31, min(2 ** 31 - 1, result * flag))


if __name__ == '__main__':
    print(Solution().myAtoi("+-123"))
