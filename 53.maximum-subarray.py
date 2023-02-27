#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.57%)
# Likes:    6255
# Dislikes: 267
# Total Accepted:    769.9K
# Total Submissions: 1.7M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        maxSum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            maxSum = dp[i] if dp[i] > maxSum else maxSum
        return maxSum


# @lc code=end
