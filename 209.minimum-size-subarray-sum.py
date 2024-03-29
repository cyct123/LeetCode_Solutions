#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.81%)
# Likes:    8723
# Dislikes: 244
# Total Accepted:    660.3K
# Total Submissions: 1.5M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
#
#
# Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
# Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
# Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#
from bisect import bisect_left
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[-1] + nums[i])
        for i in range(1, len(nums) + 1):
            s = target + sums[i - 1]
            bound = bisect_left(sums, s)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        return 0 if ans == len(nums) + 1 else ans


# @lc code=end
class WindowSolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        ans = len(nums) + 1
        total = 0
        while right != len(nums):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1
        return ans if ans != len(nums) + 1 else 0
