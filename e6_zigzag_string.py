#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/6'

"""


class Solution:
    def zigzag_string(self, str, n_rows):

        if n_rows == 1:
            return str

        buffers = [""] * n_rows
        str_len = len(str)
        i = 0

        while i < str_len:

            for j in range(n_rows):

                if i >= str_len:
                    break

                buffers[j] += str[i]
                i += 1

            for j in range(n_rows - 2, 0, -1):

                if i >= str_len:
                    break

                buffers[j] += str[i]
                i += 1

        return "".join(buffers)


if __name__ == '__main__':
    print(Solution().zigzag_string("PAYPALISHIRING", 3))
