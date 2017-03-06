#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/6'

"""


class Solution:
    def zigzag_string(self, str, n_rows):
        str_ret = ""
        str_len = len(str)
        for i in range(n_rows):
            j = i
            while j < str_len:
                str_ret += str[j]
                j = (j + n_rows + 1) if (i % 2 == 0) else (j + n_rows - (i // 2 + 1))

        return str_ret


if __name__ == '__main__':
    print(Solution().zigzag_string("PAYPALISHIRING", 3))
