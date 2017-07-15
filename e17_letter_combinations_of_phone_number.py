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

        #循环处理每一个digit
        for _, digit in enumerate(digits):
            tmp = []
            #遍历每一个digit代表的字母
            for _, c in enumerate(p_number_dict[digit]):
                #累加至已有结果
                for _, result in enumerate(results):
                    tmp.append(result + c)

            results = tmp

        return results


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))