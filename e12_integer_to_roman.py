#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/13'

"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m_list = ("", "M", "MM", "MMM")
        c_list = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
        x_list = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        i_list = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

        return m_list[num // 1000] + c_list[(num % 1000) // 100] + x_list[(num % 100) // 10] + i_list[num % 10]
