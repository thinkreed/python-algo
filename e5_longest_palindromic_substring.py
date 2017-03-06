#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/5'

"""


class Solution:
    def process_string(self, str):
        return '^' + '#' + '#'.join(str) + '#' + '$'

    def longest_palindromic_substring(self, str):
        if len(str) == 0:
            return
        elif len(str) == 1:
            return str

        center = 0
        r = 0

        t_str = self.process_string(str)
        str_len = len(t_str)
        p = [0] * str_len

        for i in range(1, str_len - 1):
            i_mirror = 2 * center - i
            p[i] = min(p[i_mirror], r - i) if r > i else 0
            # expand palindrome at center i
            while t_str[i + 1 + p[i]] == t_str[i - 1 - p[i]]:
                p[i] += 1

            # if If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > r:
                center = i
                r = i + p[i]

        max_len = 0
        i_center = 0

        for i in range(1, str_len - 1):
            if p[i] > max_len:
                max_len = p[i]
                i_center = i

        real_center = (i_center - 1 - max_len) // 2
        return str[real_center:real_center + max_len]


if __name__ == '__main__':
    s = Solution()
    print(s.longest_palindromic_substring("babcbabcbaccba"))
