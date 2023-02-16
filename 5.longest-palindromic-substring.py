#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.19%)
# Likes:    23901
# Dislikes: 1389
# Total Accepted:    2.3M
# Total Submissions: 7.1M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        isPalindrome = [
            [False if i != j else True for i in range(len(s))] for j in range(len(s))
        ]
        if len(s) <= 1:
            return s
        maxStart = 0
        maxLength = 1
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        isPalindrome[i][j] = True
                    else:
                        isPalindrome[i][j] = isPalindrome[i + 1][j - 1]
                if isPalindrome[i][j] and maxLength < j - i + 1:
                    maxStart = i
                    maxLength = j - i + 1
        return s[maxStart : maxStart + maxLength]


# @lc code=end
if __name__ == "__main__":
    s = "aaaa"
    print(Solution().longestPalindrome(s))
