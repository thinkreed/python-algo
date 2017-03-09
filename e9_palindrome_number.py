#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/9'

idea from https://discuss.leetcode.com/topic/8090/9-line-accepted-java-code-without-the-need-of-handling-overflow

"""


class Solution:
    def is_palindrome_number(self, n):

        if n < 0 or (n != 0 and n % 10 == 0):
            return False

        rev = 0

        while n > rev:
            rev = rev * 10 + n % 10
            n //= 10

        return n == rev or n == rev // 10


if __name__ == '__main__':
    print(Solution().is_palindrome_number(1221))
