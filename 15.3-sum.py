#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.64%)
# Likes:    5542
# Dislikes: 670
# Total Accepted:    770.9K
# Total Submissions: 3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        if not nums:
            return ret
        a = None
        for i in range(len(nums) - 2):
            if nums[i] == a:
                continue
            a = nums[i]
            if a > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == b:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == c:
                        k -= 1
        return ret


# @lc code=end
