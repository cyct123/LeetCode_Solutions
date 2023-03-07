#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (50.48%)
# Likes:    3271
# Dislikes: 180
# Total Accepted:    165.3K
# Total Submissions: 327.4K
# Testcase Example:  '[2,2,3,4]'
#
# Given an integer array nums, return the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a
# triangle.
#
#
# Example 1:
#
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
#
# Example 2:
#
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
import bisect
from typing import List


# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    res += right - left
                    right -= 1
        return res


# @lc code=end
class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for left in range(len(nums) - 2):
            for right in range(len(nums) - 1, left + 1, -1):
                length = nums[right] - nums[left]
                bound = bisect.bisect_right(nums, length, left, right)
                res += right - max(bound, left + 1)
        return res


if __name__ == "__main__":
    nums = [2, 2, 3, 4]
    print(Solution().triangleNumber(nums))
