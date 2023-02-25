#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#
# https://leetcode.com/problems/count-square-sum-triples/description/
#
# algorithms
# Easy (68.12%)
# Likes:    319
# Dislikes: 28
# Total Accepted:    30.9K
# Total Submissions: 45.4K
# Testcase Example:  '5'
#
# A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 +
# b^2 = c^2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b,
# c <= n.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
#
#
# Example 2:
#
#
# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and
# (8,6,10).
#
#
#
# Constraints:
#
#
# 1 <= n <= 250
#
#
#
from math import sqrt


# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int(sqrt(a * a + b * b + 1))
                if c <= n and a * a + b * b == c * c:
                    count += 1
        return count


# @lc code=end
