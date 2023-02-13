#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (47.18%)
# Likes:    13146
# Dislikes: 730
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        dummy = ListNode()
        cur = head
        for _ in range(length // 2):
            postNode = dummy.next
            dummy.next = cur
            cur = cur.next
            dummy.next.next = postNode
        if length % 2:
            cur = cur.next
        dummy = dummy.next
        while dummy and cur and dummy.val == cur.val:
            dummy = dummy.next
            cur = cur.next
        if cur or dummy:
            return False
        return True


# @lc code=end
