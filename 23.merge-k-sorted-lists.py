#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (38.00%)
# Likes:    3694
# Dislikes: 235
# Total Accepted:    543.7K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#

import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        hq = []
        head = tail = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(hq, (l.val, l))
        while hq:
            node = heapq.heappop(hq)[1]
            tail.next = node
            tail = tail.next
            nextNode = node.next
            if nextNode:
                heapq.heappush(hq, (nextNode.val, nextNode))
        return head.next


# @lc code=end
