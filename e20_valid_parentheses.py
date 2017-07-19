#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/22'

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in range(len(s)):
            #将对应的另一半括号压栈
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else:
                #如果最先出栈的不是和当前元素相同的括号，则不匹配
                if not stack or stack.pop() != s[i]:
                    return False
        #栈为空，所有的括号都已经匹配
        return True if not stack else False
