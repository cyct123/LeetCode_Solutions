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

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        num = set(nums)
        while num:
            n = num.pop()
            lenLeft = lenRight = 0
            i = n + 1
            while i in num:
                num.remove(i)
                lenRight += 1
                i += 1
            i = n - 1
            while i in num:
                num.remove(i)
                lenLeft += 1
                i -= 1
            maxLen = max(maxLen, lenLeft + lenRight + 1)
        return maxLen

# @lc code=end

