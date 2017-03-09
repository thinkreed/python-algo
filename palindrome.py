#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/9'

"""


class Solution:
    def is_palindrome(self, s):

        if not s:
            return False

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    print(Solution().is_palindrome("abbba"))
