#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (36.66%)
# Likes:    4269
# Dislikes: 3361
# Total Accepted:    1.1M
# Total Submissions: 3M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low, high = 1, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid == x / mid:
                return mid
            elif mid < x / mid:
                low = mid + 1
            else:
                high = mid - 1
        return high


# @lc code=end
