#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (39.61%)
# Likes:    990
# Dislikes: 257
# Total Accepted:    195.3K
# Total Submissions: 491.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(None)
        dummy = ListNode(None)
        large = dummy
        small.next = head
        prev = small
        while small.next:
            cur = small.next
            if cur.val >= x:
                large.next = cur
                large = large.next
                small.next = small.next.next
            else:
                small = small.next
        large.next = None
        small.next = dummy.next
        return prev.next

# @lc code=end

