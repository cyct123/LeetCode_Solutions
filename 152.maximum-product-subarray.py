#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.90%)
# Likes:    15262
# Dislikes: 457
# Total Accepted:    959K
# Total Submissions: 2.7M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = nums[0]
        dpMin = nums[0]
        ret = nums[0]
        for i in range(1, len(nums)):
            tempMax = dpMax
            tempMin = dpMin
            dpMax = max(tempMax * nums[i], nums[i], tempMin * nums[i])
            dpMin = min(tempMax * nums[i], nums[i], tempMin * nums[i])
            ret = max(dpMax, ret)
        return ret


# @lc code=end


class FirstSolution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [0] * len(nums)
        dpMin = [0] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        for i in range(1, len(nums)):
            dpMax[i] = max(dpMax[i - 1] * nums[i], nums[i], dpMin[i - 1] * nums[i])
            dpMin[i] = min(dpMax[i - 1] * nums[i], nums[i], dpMin[i - 1] * nums[i])
        return max(dpMax)


if __name__ == "__main__":
    nums = [-2, 0, -1]
    print(Solution().maxProduct(nums))
