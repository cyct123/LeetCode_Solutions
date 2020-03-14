#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (37.15%)
# Likes:    1864
# Dislikes: 121
# Total Accepted:    244.8K
# Total Submissions: 655K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        start = dummy
        prev = start.next
        i = 0
        while head:
            cur = head
            head = head.next
            if i < m - 1:
                start = start.next
                prev = start.next
            elif m <= i <= n - 1:
                post = start.next
                start.next = cur
                prev.next = cur.next
                cur.next = post
            i += 1
        return dummy.next


# @lc code=end

