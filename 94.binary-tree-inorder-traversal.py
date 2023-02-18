#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (60.57%)
# Likes:    2504
# Dislikes: 105
# Total Accepted:    631K
# Total Submissions: 1M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
from typing import List


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


# iterative solutioon
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        vals = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                vals.append(node.val)
                root = node.right
        return vals


# @lc code=end


class recursiveSolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        vals = []
        if not root:
            return vals
        vals.extend(self.inorderTraversal(root.left))
        vals.append(root.val)
        vals.extend(self.inorderTraversal(root.right))
        return vals
