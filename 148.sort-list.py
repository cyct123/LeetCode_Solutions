#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (52.61%)
# Likes:    9206
# Dislikes: 280
# Total Accepted:    600.5K
# Total Submissions: 1.1M
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
#
#
# Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
#
# Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
#
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)

    def mergeSort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        leftHead, rightHead = head, slow.next
        slow.next = None
        return self.merge(self.mergeSort(leftHead), self.mergeSort(rightHead))

    def merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        while left and right:
            if left.val <= right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev.next.next = None
            prev = prev.next
        if left:
            prev.next = left
        if right:
            prev.next = right
        return dummy.next


# @lc code=end
if __name__ == "__main__":
    nums = [4, 2, 1, 3]
    dummy = ListNode()
    cur = dummy
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    head = Solution().sortList(dummy.next)
    while head:
        print(head.val)
        head = head.next
