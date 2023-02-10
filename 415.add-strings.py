#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (52.33%)
# Likes:    4185
# Dislikes: 630
# Total Accepted:    546.7K
# Total Submissions: 1M
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
#
#
# Example 1:
#
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
#
# Example 2:
#
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
#
# Example 3:
#
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
#
#
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while carry or i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            i -= 1
            j -= 1
            num = n1 + n2 + carry
            carry = num // 10
            ret.append(str(num % 10))
        return "".join(ret[::-1])


# @lc code=end
if __name__ == "__main__":
    Solution().addStrings("11", "123")
