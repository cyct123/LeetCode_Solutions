#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (55.72%)
# Likes:    2433
# Dislikes: 201
# Total Accepted:    502.7K
# Total Submissions: 901.7K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = nums[0]
        count = 0
        for num in nums:
            if ret != num:
                count -= 1
                if not count:
                    ret = num
                    count += 1
            else:
                count += 1
        return ret


# @lc code=end
