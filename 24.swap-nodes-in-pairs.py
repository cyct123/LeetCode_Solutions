#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (48.10%)
# Likes:    1733
# Dislikes: 152
# Total Accepted:    406.2K
# Total Submissions: 844K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        prev = dummy
        dummy.next = head
        while head and head.next:
            slow = head
            fast = head.next
            head = fast.next
            slow.next = head
            fast.next = slow
            prev.next = fast
            prev = slow
        return dummy.next

# @lc code=end

