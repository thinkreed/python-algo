#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/21'

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        thanks to https://discuss.leetcode.com/topic/14692/3-short-python-solutions
        """

        #一个快，一个慢
        fast = slow = head
        #先让快的比慢的先走n个
        for _ in range(n):
            fast = fast.next
        #整个链表长度等于n，所以倒数第n个就是头部
        if not fast:
            return head.next
        #当循环结束时，慢指针slow恰好走到倒数第n个
        while fast.next:
            fast = fast.next
            slow = slow.next
        #删除倒数第n个
        slow.next = slow.next.next

        return head
