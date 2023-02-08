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
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        gap = len(nums) // 2
        while gap:
            for i in range(gap, len(nums)):
                temp = nums[i]
                j = i
                while j >= gap and nums[j-gap] > temp:
                    nums[j] = nums[j-gap]
                    j -= gap
                nums[j] = temp
            gap //= 2
        return nums


# @lc code=end

