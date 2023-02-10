#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.82%)
# Likes:    32003
# Dislikes: 1404
# Total Accepted:    4.2M
# Total Submissions: 12.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = right = 0
        ans = 0
        while right != len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans

# @lc code=end

