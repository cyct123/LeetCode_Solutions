#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (40.66%)
# Likes:    2608
# Dislikes: 154
# Total Accepted:    224.5K
# Total Submissions: 550.3K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxValues = []
        if not nums:
            return maxValues
        maxValue = max(nums[:k])
        maxValues.append(maxValue)
        prevHead = 0
        newEnd = k
        while newEnd < len(nums):
            if nums[prevHead] == maxValue:
                maxValue = max(nums[prevHead+1: newEnd+1])
            elif nums[newEnd] > maxValue:
                maxValue = nums[newEnd]
            maxValues.append(maxValue)
            prevHead += 1
            newEnd += 1
        return maxValues

# @lc code=end

