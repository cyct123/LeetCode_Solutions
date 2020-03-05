#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (66.66%)
# Likes:    1995
# Dislikes: 133
# Total Accepted:    221.1K
# Total Submissions: 330.9K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
#
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        multiple2 = 1
        for i in range(1, num+1):
            if i == multiple2:
                dp[i] = 1
                multiple2 *= 2
            else:
                dp[i] = 1 + dp[i - multiple2 // 2]
        return dp

# @lc code=end

