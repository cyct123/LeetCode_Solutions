#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (39.76%)
# Likes:    1405
# Dislikes: 423
# Total Accepted:    406.2K
# Total Submissions: 1M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
#
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, total = queue.popleft()
            if not node.left and not node.right and total == sum:
                return True
            if node.left:
                queue.append((node.left, total + node.left.val))
            if node.right:
                queue.append((node.right, total + node.right.val))
        return False


# @lc code=end


class RecursiveSolution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val != sum:
                return False
            else:
                return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )


class StackIterasiveSolution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()
            if not node.left and not node.right and total == sum:
                return True
            if node.left:
                stack.append((node.left, total + node.left.val))
            if node.right:
                stack.append((node.right, total + node.right.val))
        return False
