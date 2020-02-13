#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        while l1 or l2:
            if l1 and l2:
                v1 = l1.val
                v2 = l2.val
                smaller = min(v1, v2)
                new_node = ListNode(smaller)
                cur.next = new_node
                cur = cur.next
                if v1 < v2:
                    l1 = l1.next
                else:
                    l2 = l2.next
            elif l1:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        return dummy.next
# @lc code=end

