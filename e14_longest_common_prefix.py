#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/15'

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        #获取最短和最长的str
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            #不同，截至i
            if c != s2[i]:
                return s1[:i]

        return s1

    def method2(self, strs):

        if not strs:
            return ''

        for i in range(len(strs[0])):

            c = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]

        return strs[0]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["c", "c"]))
