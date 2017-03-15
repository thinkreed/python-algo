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

        ret = strs[0]

        for i in range(1, len(strs)):
            tmp_sub = ""
            index = 0

            if len(ret) > 0 and len(strs[i]) > 0:
                while ret[index] == strs[i][index]:
                    tmp_sub += ret[index]
                    index += 1
                    if index >= len(ret) or index >= len(strs[i]):
                        break

                ret = tmp_sub

        return ret


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["c", "c"]))
