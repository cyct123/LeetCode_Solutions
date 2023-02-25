#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Medium (33.07%)
# Likes:    6461
# Dislikes: 1238
# Total Accepted:    708K
# Total Submissions: 2.1M
# Testcase Example:  '10'
#
# Given an integer n, return the number of prime numbers that are strictly less
# than n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [True] * n
        count = 0
        for i in range(2, n):
            if isPrimes[i]:
                count += 1
                for j in range(i * i, n, i):
                    isPrimes[j] = False
        return count


# @lc code=end
