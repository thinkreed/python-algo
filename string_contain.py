#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/10'

"""


def is_contain(s, t):
    if not s:
        return -1

    if not t:
        return -1

    t_c = t[0]

    for j, s_c in enumerate(s):
        if s_c == t_c:
            t_index = 1
            s_index = j + 1
            while t_index < len(t):
                if s_index == len(s) or s[s_index] != t[t_index]:
                    return -1
                t_index += 1
                s_index += 1
            return j
    return -1
