#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/19'

idea from https://discuss.leetcode.com/topic/22705/python-140ms-beats-100-and-works-for-n-sum-n-2/4
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def find_N_sum(nums, start, target, n, result, results):
            if len(nums[start:]) < n or n < 2 or target < nums[start] * n or target > nums[-1] * n:
                return
            elif n == 2:
                left, right = start, len(nums) - 1

                while left < right:
                    cur_sum = nums[left] + nums[right]

                    if cur_sum < target:
                        left += 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                pass
            else:
                for i in range(len(nums[start:]) - n + 1):
                    if i == 0 or (i > 0 and nums[start + i - 1] != nums[start + i]):
                        find_N_sum(nums, start + i + 1, target - nums[start + i], n - 1, result + [nums[start + i]],
                                   results)

        results = []
        find_N_sum(sorted(nums), 0, target, 4, [], results)
        return results


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
