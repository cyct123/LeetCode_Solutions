#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (34.39%)
# Likes:    1074
# Dislikes: 89
# Total Accepted:    205.8K
# Total Submissions: 598.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        prev_val = prev.val
        while head:
            if prev_val != head.val and ((not head.next) or (head.val != head.next.val)):
                prev.next = head
                prev = head
            prev_val = head.val
            head = head.next
        prev.next = head
        return dummy.next

# @lc code=end

