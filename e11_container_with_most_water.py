#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/12'

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            if height[left] < height[right]:
                cur_area = height[left] * (right - left)
                left += 1
            else:
                cur_area = height[right] * (right - left)
                right -= 1
            max_area = max(max_area, cur_area)

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 1]))
