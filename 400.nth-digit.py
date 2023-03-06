#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Medium (34.12%)
# Likes:    847
# Dislikes: 1780
# Total Accepted:    83.8K
# Total Submissions: 245.5K
# Testcase Example:  '3'
#
# Given an integer n, return the n^th digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
#
#
# Example 2:
#
#
# Input: n = 11
# Output: 0
# Explanation: The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, ... is a 0, which is part of the number 10.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digits += 1
            start *= 10
            base = start * digits * 9
        num = start + (n - 1) // digits
        index = (n - 1) % digits
        return int(str(num)[index])


# @lc code=end
