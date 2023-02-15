#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (41.77%)
# Likes:    5309
# Dislikes: 688
# Total Accepted:    501.8K
# Total Submissions: 1.2M
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value.
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        op = "+"
        stack = []
        index = 0
        while index != len(s):
            if s[index] == " ":
                index += 1
                continue
            if s[index].isdigit():
                num = ord(s[index]) - ord("0")
                while index + 1 != len(s) and s[index + 1].isdigit():
                    index += 1
                    num = num * 10 + ord(s[index]) - ord("0")
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-1 * num)
                elif op == "*":
                    prev_num = stack.pop()
                    stack.append(prev_num * num)
                else:
                    prev_num = stack.pop()
                    stack.append(int(prev_num / num))
            if s[index] in "+-*/":
                op = s[index]
            index += 1
        return sum(stack)


# @lc code=end
if __name__ == "__main__":
    s = " 3 + 5 / 2 "
    print(Solution().calculate(s))
