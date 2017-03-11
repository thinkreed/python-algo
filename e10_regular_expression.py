#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/10'

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        great thanks to https://discuss.leetcode.com/topic/40371/easy-dp-java-solution-with-detailed-explanation/2
        and https://discuss.leetcode.com/topic/6183/my-concise-recursive-and-dp-solutions-with-full-explanation-in-c/2
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    if p[i - 1] != s[j] and p[i - 1] != '.':
                        dp[i + 1][j + 1] = dp[i - 1][j + 1]
                    else:
                        dp[i + 1][j + 1] = dp[i][j + 1] or dp[i - 1][j + 1] or dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isMatch("aab", "c*a*b"))
