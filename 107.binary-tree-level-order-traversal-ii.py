#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (49.79%)
# Likes:    1030
# Dislikes: 186
# Total Accepted:    277.1K
# Total Submissions: 555.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        vals = []
        if not root:
            return vals
        stack = [[root]]
        while stack:
            nodes = stack[-1]
            newNodes = []
            for node in nodes:
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            if newNodes:
                stack.append(newNodes)
            else:
                break
        while stack:
            nodes = stack.pop()
            v = []
            for node in nodes:
                v.append(node.val)
            if v:
                vals.append(v)
        return vals
# @lc code=end

