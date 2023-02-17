#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (39.02%)
# Likes:    5821
# Dislikes: 2582
# Total Accepted:    632.1K
# Total Submissions: 1.6M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
#
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
#
#
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for j in range(len(num2) - 1, -1, -1):
            subProduct = 0
            n2 = ord(num2[j]) - ord("0")
            for i in range(len(num1) - 1, -1, -1):
                n1 = ord(num1[i]) - ord("0")
                subProduct += n1 * n2 * 10 ** (len(num1) - 1 - i)
            product += subProduct * 10 ** (len(num2) - 1 - j)
        return str(product)


# @lc code=end
if __name__ == "__main__":
    print(Solution().multiply("123", "456"))
