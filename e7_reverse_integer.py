#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/7'

"""


class Solution:
    def reverse_integer(self, value):
        ret_val = 0
        flag = 1
        if value < 0:
            value *= -1
            flag = -1

        while value != 0:
            tail = value % 10
            cur = ret_val * 10 + tail
            check = cur // 10
            if check != ret_val:
                return 0
            ret_val = cur
            value = (value // 10)

        return ret_val * flag


if __name__ == '__main__':
    print(Solution().reverse_integer(-123))
