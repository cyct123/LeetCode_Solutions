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

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            val = d.get(i, 0)
            val += 1
            d[i] = val
        majority_element = None
        max_appearance = 0
        for k, v in d.items():
            if not majority_element or max_appearance < v:
                majority_element = k
                max_appearance = v
        return majority_element
# @lc code=end

