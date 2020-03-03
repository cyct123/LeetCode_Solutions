#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (42.47%)
# Likes:    1760
# Dislikes: 146
# Total Accepted:    398.6K
# Total Submissions: 937.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.helper(root.left) - self.helper(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self, root):
        if not root:
            return 0
        heights = 1
        nodes = [root]
        while nodes:
            newNodes = []
            for node in nodes:
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            if newNodes:
                heights += 1
            nodes = newNodes
        return heights

# @lc code=end

