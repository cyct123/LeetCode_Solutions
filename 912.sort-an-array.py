#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (58.52%)
# Likes:    3260
# Dislikes: 602
# Total Accepted:    355.2K
# Total Submissions: 607.1K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
#
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
#
#
# Example 1:
#
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
#
#
# Example 2:
#
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#

from typing import List
import random
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], start: int, end:int):
        if start < end:
            pivot_index = self.randomPartition(nums, start, end)
            self.quickSort(nums, start, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, end)
        return nums

    def randomPartition(self, nums: List[int], start: int, end: int) -> int:
        i = random.randint(start, end)
        nums[i], nums[start] = nums[start], nums[i]
        return self.partition(nums, start, end)

    def partition(self, nums: List[int], start: int, end: int) -> int:
        pivot = nums[start]
        i = start + 1
        for j in range(i, end+1):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[start], nums[i-1] = nums[i-1], nums[start]
        return i - 1




# @lc code=end

