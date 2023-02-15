#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (56.58%)
# Likes:    10322
# Dislikes: 459
# Total Accepted:    615.8K
# Total Submissions: 1.1M
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
#
# The test cases are generated so that the length of the output will never
# exceed 10^5.
#
#
# Example 1:
#
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
#
# Example 2:
#
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
#
# Example 3:
#
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
#
#
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        subStrs = []
        index = 0
        while index != len(s):
            if s[index].isdigit():
                num = ord(s[index]) - ord("0")
                while index + 1 != len(s) and s[index + 1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord("0")
                nums.append(num)
            elif s[index] == "]":
                letters = []
                while subStrs[-1] != "[":
                    letters.append(subStrs.pop())
                subStrs.pop()
                repeated = nums.pop()
                subStrs.append("".join(letters[::-1]) * repeated)
            else:
                subStrs.append(s[index])
            index += 1
        return "".join(subStrs)


# @lc code=end
