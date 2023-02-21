#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (59.12%)
# Likes:    5392
# Dislikes: 96
# Total Accepted:    532.3K
# Total Submissions: 899.4K
# Testcase Example:  '[1,2,3]'
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
#
#
# Return the total sum of all root-to-leaf numbers. Test cases are generated so
# that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
#
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
#
#
#
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        res = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                res.append(self.pathSum(path))
            dfs(root.left)
            dfs(root.right)
            path.pop()

        dfs(root)
        return sum(res)

    def pathSum(self, path: List[int]):
        total = 0
        for i in range(len(path)):
            total = total * 10 + path[i]
        return total


# @lc code=end
if __name__ == "__main__":
    nums = [4, 9, 0, 5, 1]
    root = None
    queue = deque()
    for i in range(len(nums)):
        node = TreeNode(nums[i])
        if not root:
            root = node
        else:
            prev = queue[0]
            if i % 2:
                prev.left = node
            else:
                prev.right = node
                queue.popleft()
        queue.append(node)
    print(Solution().sumNumbers(root))
