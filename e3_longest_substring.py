#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/3'

"""


class Solution:
    def longest_substring(self, str):

        start = max_length = 0
        usedChar = {}

        for i in range(len(str)):
            if str[i] in usedChar:
                start = usedChar[str[i]] + 1

            max_length = max(max_length, i - start + 1)
            usedChar[str[i]] = i

        return max_length


if __name__ == '__main__':
    print(Solution().longest_substring("pwwkew"))
