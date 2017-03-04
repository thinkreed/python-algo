#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/4'

"""


class Solution:
    def find_median_of_two_array(self, arr1, arr2):
        m, n = len(arr1), len(arr2)
        if m > n:
            arr1, arr2, m, n = arr2, arr1, n, m
        if n == 0:
            raise ValueError
        left, right, len_half = 0, m, (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = len_half - i
            if i < m and arr2[j - 1] > arr1[i]:
                left = i + 1
            elif i > 0 and arr1[i - 1] > arr2[j]:
                right = i - 1
            else:
                if i == 0:
                    max_of_left = arr2[j - 1]
                elif j == 0:
                    max_of_left = arr1[i - 1]
                else:
                    max_of_left = max(arr1[i - 1], arr2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = arr2[j]
                elif j == n:
                    min_of_right = arr1[i]
                else:
                    min_of_right = min(arr1[i], arr2[j])
                return (min_of_right + max_of_left) / 2


if __name__ == '__main__':
    arr1 = [1, 3]
    arr2 = [2]
    print(Solution().find_median_of_two_array(arr1, arr2))
