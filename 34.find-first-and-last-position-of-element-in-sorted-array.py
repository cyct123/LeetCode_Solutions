#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (34.99%)
# Likes:    2579
# Dislikes: 116
# Total Accepted:    420K
# Total Submissions: 1.2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if index == -1:
            return [-1, -1]
        i = index
        while i >= 0 and nums[i] == target:
            i -= 1
        j = index
        while j != len(nums) and nums[j] == target:
            j += 1
        return [i + 1, j - 1]


# @lc code=end
