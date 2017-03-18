#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/18'

"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        p_number_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

        results = ['']

        for _, digit in enumerate(digits):
            tmp = []
            for _, c in enumerate(p_number_dict[digit]):
                for _, result in enumerate(results):
                    tmp.append(result + c)

            results = tmp

        return results


if __name__ == '__main__':
    Solution().letterCombinations("23")
