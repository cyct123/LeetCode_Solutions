#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.01%)
# Likes:    4169
# Dislikes: 196
# Total Accepted:    860.7K
# Total Submissions: 2.3M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []
        leftPar = "([{"
        rightPar = ")]}"
        for token in s:
            if token in leftPar:
                parStack.append(token)
            else:
                if not parStack:
                    return False
                par = parStack.pop()
                if leftPar.index(par) != rightPar.index(token):
                    return False
        return not parStack

# @lc code=end
