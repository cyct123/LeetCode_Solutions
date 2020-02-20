#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (33.93%)
# Likes:    901
# Dislikes: 2490
# Total Accepted:    487.7K
# Total Submissions: 1.4M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            head = s[i].lower()
            if not (head.islower() or head.isdigit()):
                i += 1
                continue
            tail = s[j].lower()
            if not (tail.islower() or tail.isdigit()):
                j -= 1
                continue
            if head != tail:
                return False
            i += 1
            j -= 1
        return True

# @lc code=end

