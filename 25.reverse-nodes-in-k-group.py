#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (54.26%)
# Likes:    10346
# Dislikes: 560
# Total Accepted:    654.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        countNode = head
        while (countNode):
            count += 1
            countNode = countNode.next
        if not count:
            return head
        swapRound = count // k
        dummyNode = ListNode()
        prevNode = dummyNode
        curNode = head
        lastNode = None
        for i in range(swapRound):
            for j in range(k):
                if not j:
                    lastNode = curNode
                nextNode = prevNode.next
                prevNode.next = curNode
                curNode = curNode.next
                prevNode.next.next = nextNode
            prevNode = lastNode
        prevNode.next = curNode
        return dummyNode.next

# @lc code=end

