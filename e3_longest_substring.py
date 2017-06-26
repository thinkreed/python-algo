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
        # 已出现过的字符字典, char -> index
        usedChar = {}

        for i in range(len(str)):
            # 如果出现重复，从当前的后一位开始计算
            if str[i] in usedChar:
                start = usedChar[str[i]] + 1

            # 最大长度计数，并将当前字符加入字典
            max_length = max(max_length, i - start + 1)
            usedChar[str[i]] = i

        return max_length


if __name__ == '__main__':
    print(Solution().longest_substring("pwwkew"))
