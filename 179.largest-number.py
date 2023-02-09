#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (33.20%)
# Likes:    6442
# Dislikes: 529
# Total Accepted:    376.5K
# Total Submissions: 1.1M
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of
# an integer.
#
#
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            max_index = i
            for j in range(i + 1, len(nums)):
                if self.isSmaller(nums[max_index], nums[j]):
                    max_index = j
            if max_index != i:
                nums[i], nums[max_index] = nums[max_index], nums[i]
        i = 0
        while i != len(nums) and nums[i] == "0":
            i += 1
        i = i - 1 if i != 0 else 0
        return "".join(nums[i:])

    def isSmaller(self, str1: str, str2: str) -> bool:
        i = 0
        while i != len(str1) + len(str2) - 1:
            if i < len(str1):
                char1 = str1[i]
            else:
                char1 = str2[i - len(str1)]
            if i < len(str2):
                char2 = str2[i]
            else:
                char2 = str1[i - len(str2)]
            if char1 < char2:
                return True
            elif char1 > char2:
                return False
            i += 1
        return False


# @lc code=end
if __name__ == "__main__":
    nums = [10, 2]
    print(Solution().largestNumber(nums))
