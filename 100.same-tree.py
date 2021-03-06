#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (51.73%)
# Likes:    1657
# Dislikes: 49
# Total Accepted:    481.9K
# Total Submissions: 930.6K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
#
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
#
# Example 1:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
#
# ⁠       [1,2,3],   [1,2,3]
#
# Output: true
#
#
# Example 2:
#
#
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
#
# ⁠       [1,2],     [1,null,2]
#
# Output: false
#
#
# Example 3:
#
#
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
#
# ⁠       [1,2,1],   [1,1,2]
#
# Output: false
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

class iterativeSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.order(p) == self.order(q)

    def order(self, root: TreeNode) -> bool:
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append(None)
        return res

# @lc code=end

class recursiveSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.order(p) == self.order(q)

    def order(self, p: TreeNode) -> List[int]:
        o = []
        if p:
            o.append(p.val)
            o.extend(self.order(p.left))
            o.extend(self.order(p.right))
        else:
            o.append(None)
        return o

