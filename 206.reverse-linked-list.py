#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (59.36%)
# Likes:    3502
# Dislikes: 78
# Total Accepted:    817.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = cur = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return cur

# @lc code=end

