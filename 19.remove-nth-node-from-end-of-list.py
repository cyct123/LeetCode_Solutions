#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            slow = ListNode(None)
            slow.next = head
            dummy = slow
            fast = head
            for _ in range(n):
                fast = fast.next
            while fast:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        return dummy.next

# @lc code=end

