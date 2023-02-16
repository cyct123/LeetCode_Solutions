#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (43.71%)
# Likes:    2570
# Dislikes: 148
# Total Accepted:    259.7K
# Total Submissions: 594.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)
        while numSet:
            curLen = 1
            num = numSet.pop()
            left = num - 1
            right = num + 1
            while left in numSet:
                curLen += 1
                numSet.remove(left)
                left = left - 1
            while right in numSet:
                curLen += 1
                numSet.remove(right)
                right = right + 1
            maxLen = curLen if curLen > maxLen else maxLen
        return maxLen


# @lc code=end
