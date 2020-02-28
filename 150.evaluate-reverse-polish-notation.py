#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (34.58%)
# Likes:    796
# Dislikes: 418
# Total Accepted:    202K
# Total Submissions: 583.2K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
#
# Note:
#
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
#
#
# Example 1:
#
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = []
        for token in tokens:
            if token not in "+-*/":
                nums.append(int(token))
            else:
                b = nums.pop()
                a = nums.pop()
                nums.append(self.doMath(token, a, b))
        return nums[-1]

    def doMath(self, token, a, b):
        if token == '+':
            return a + b
        elif token == '-':
            return a - b
        elif token == '*':
            return a * b
        else:
            return int(a / b)
# @lc code=end

