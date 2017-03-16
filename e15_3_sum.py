#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/16'

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()
        i = 0

        while i < len(nums):
            target = 0 - nums[i]

            if target < 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    triple = [nums[i], nums[left], nums[right]]

                    while left < right and nums[left] == triple[1]:
                        left += 1

                    while left < right and nums[right] == triple[2]:
                        right -= 1

                    result.append(triple)

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            i += 1

        return result


if __name__ == '__main__':
    print(Solution().threeSum([1, 2, -2, -1]))
