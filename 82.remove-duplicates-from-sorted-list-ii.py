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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        prevNode = head
        curNode = head.next
        count = 1
        dummyNode = ListNode(None)
        newHead = dummyNode
        while curNode:
            if prevNode.val == curNode.val:
                count += 1
            else:
                if count == 1:
                    newHead.next = prevNode
                    prevNode.next = None
                    newHead = newHead.next
                prevNode = curNode
                count = 1
            curNode = curNode.next
        if count == 1:
            newHead.next = prevNode
            prevNode.next = None
            newHead = newHead.next
        return dummyNode.next


# @lc code=end
