#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (59.51%)
# Likes:    4479
# Dislikes: 244
# Total Accepted:    500.1K
# Total Submissions: 824.3K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(s="", left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtracking(s + "(", left + 1, right)
            if right < left:
                backtracking(s + ")", left, right + 1)

        backtracking()
        return res


# @lc code=end
