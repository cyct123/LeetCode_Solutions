#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.05%)
# Likes:    6215
# Dislikes: 1620
# Total Accepted:    1.1M
# Total Submissions: 3.3M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carrier = 0
        total = 0
        head = cur = None
        while (l1 or l2 or carrier):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carrier
            carrier = total // 10
            dummy = ListNode(total % 10)
            if not head:
                head = cur = dummy
            else:
                cur.next = dummy
                cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head
            
# @lc code=end

