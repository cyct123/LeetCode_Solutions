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
        self.maxHeapSort(nums)
        return nums

    def maxHeapSort(self, nums: List[int]):
        self.buildMaxHeap(nums)
        for i in range(len(nums)-1):
            nums[0], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[0]
            self.heapify(nums, 0, len(nums) - 2 - i)

    def buildMaxHeap(self, nums:List[int]):
        for i in range(len(nums) // 2, -1, -1):
            self.heapify(nums, i, len(nums)-1)

    def heapify(self, nums: List[int], index: int, end: int):
        left_index = index * 2 + 1
        right_index = left_index + 1
        while left_index <= end:
            max_index = index
            if nums[left_index] > nums[max_index]:
                max_index = left_index
            if right_index <= end and nums[right_index] > nums[max_index]:
                max_index = right_index
            if max_index == index:
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            index = max_index
            left_index = index * 2 + 1
            right_index = left_index + 1

# @lc code=end

if __name__ == "__main__":
    nums = [-4,0,7,4,9,-5,-1,0,-7,-1]
    print(Solution().sortArray(nums))

