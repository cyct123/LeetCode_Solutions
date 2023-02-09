#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.87%)
# Likes:    19741
# Dislikes: 1193
# Total Accepted:    1.9M
# Total Submissions: 4.9M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
#
#
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        min_index = self.searchMin(nums)
        if nums[0] > target:
            return self.binarySearch(nums, min_index, len(nums) - 1, target)
        else:
            return self.binarySearch(nums, 0, (min_index - 1 + len(nums)) % len(nums), target)

    def searchMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low

    def binarySearch(self, nums: List[int], low: int, high: int, target: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# @lc code=end
if __name__ == "__main__":
    nums = [1, 3]
    target = 3
    print(Solution().search(nums, target))

