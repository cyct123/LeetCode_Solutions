#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (63.82%)
# Likes:    1983
# Dislikes: 67
# Total Accepted:    697.8K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterative solution
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, depth = [(root, 1)], 0
        while stack:
            node, curDepth = stack.pop()
            if node:
                depth = max(depth, curDepth)
                if node.right:
                    stack.append((node.right, curDepth+1))
                if node.left:
                    stack.append((node.left, curDepth+1))
        return depth


# @lc code=end

# recursive solution
class recursiveSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
