#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (58.71%)
# Likes:    2454
# Dislikes: 169
# Total Accepted:    324.3K
# Total Submissions: 548.5K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Note:
#
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#
#
#

# @lc code=start
import heapq
import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            count = freq.get(num, 0)
            count += 1
            freq[num] = count
        return [k for k, _ in heapq.nlargest(k, freq.items(), key=operator.itemgetter(1))]

# @lc code=end

