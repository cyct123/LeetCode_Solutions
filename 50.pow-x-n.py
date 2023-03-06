#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (32.92%)
# Likes:    6779
# Dislikes: 7089
# Total Accepted:    1.2M
# Total Submissions: 3.5M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
# Constraints:
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# -10^4 <= x^n <= 10^4
#
#
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return x
        res = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


# @lc code=end
