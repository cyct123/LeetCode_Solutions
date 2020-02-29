#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (45.06%)
# Likes:    1546
# Dislikes: 84
# Total Accepted:    302.8K
# Total Submissions: 670.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nums = []
        if not root:
            return nums
        stack = [[root]]
        i = 0
        while stack:
            vals = []
            children = []
            nodes = stack.pop()
            for node in nodes:
                vals.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if children:
                stack.append(children)
            if vals:
                if i % 2 == 1:
                    nums.append(vals[::-1])
                else:
                    nums.append(vals)
            i += 1
        return nums
# @lc code=end

