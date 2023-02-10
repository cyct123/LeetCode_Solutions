#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (45.53%)
# Likes:    5068
# Dislikes: 161
# Total Accepted:    216.6K
# Total Submissions: 475.5K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is
# strictly less than k.
#
#
# Example 1:
#
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3], k = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#
from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count = 0
        left = right = 0
        product = 1
        while right != len(nums):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count

# @lc code=end

if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))

