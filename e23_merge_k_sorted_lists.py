#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/24'

"""

from queue import PriorityQueue


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        from https://discuss.leetcode.com/topic/33609/10-line-python-solution-with-priority-queue
        """

        head = cur = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))

        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next

            if cur.next:
                q.put((cur.next.val, cur.next))

        return head.next
