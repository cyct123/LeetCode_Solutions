#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (37.37%)
# Likes:    14475
# Dislikes: 4038
# Total Accepted:    998.7K
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
#
#
# For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
#
#
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
#
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
#
#
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
#
#
# Example 3:
#
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#
from typing import List


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                j = i + 1
                break
        if j != -1:
            for k in range(len(nums) - 1, j - 1, -1):
                if nums[k] > nums[j - 1]:
                    nums[k], nums[j - 1] = nums[j - 1], nums[k]
                    break
            for i in range((len(nums) - j) // 2):
                nums[j + i], nums[len(nums) - 1 - i] = (
                    nums[len(nums) - 1 - i],
                    nums[j + i],
                )
        else:
            nums.reverse()


# @lc code=end
if __name__ == "__main__":
    nums = [1, 3, 2]
    Solution().nextPermutation(nums)
    print(nums)
