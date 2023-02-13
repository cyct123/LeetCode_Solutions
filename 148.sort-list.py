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
from typing import Optional, Tuple


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
        pass

    def splitList(
        self, head: Optional[ListNode]
    ) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        left = ListNode()
        right = ListNode()
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        cur = head
        leftCur = left
        rightCur = right
        for i in range(length):
            if i <= length // 2:
                leftCur.next = cur
                cur = cur.next
                leftCur.next.next = None
                leftCur = leftCur.next
            else:
                rightCur.next = cur
                cur = cur.next
                rightCur.next.next = None
                rightCur = rightCur.next
        return left.next, right.next


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
