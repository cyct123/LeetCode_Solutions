#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.57%)
# Likes:    2118
# Dislikes: 2373
# Total Accepted:    344.4K
# Total Submissions: 1.5M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] >= "1":
                if i == 0:
                    dp[i] = 1
                else:
                    dp[i] = dp[i-1]
            if i > 0 and "10" <= s[i-1: i+1] <= "26":
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]

# @lc code=end

