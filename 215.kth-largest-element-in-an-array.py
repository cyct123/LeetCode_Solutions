#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (52.17%)
# Likes:    2918
# Dislikes: 208
# Total Accepted:    520.9K
# Total Submissions: 997.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#
from typing import List
from random import randint

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickStort(nums, 0, len(nums)-1, len(nums)-k)

    def quickStort(self, nums: List[int], low: int, high: int, index: int) -> int:
        if low < high:
            pi = self.randomPartition(nums, low, high)
            if pi == index:
                return nums[pi]
            elif pi > index:
                return self.quickStort(nums, low, pi - 1, index)
            else:
                return self.quickStort(nums, pi + 1, high, index)


    def randomPartition(self, nums: List[int], low: int, high: int) -> int:
        pi = randint(low, high)
        nums[low], nums[pi] = nums[pi], nums[low]
        return self.partition(nums, low, high)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[low]
        i = low + 1
        for j in range(i, high+1):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[low], nums[i-1] = nums[i-1], nums[low]
        return i - 1

# @lc code=end

