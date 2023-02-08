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

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        for i in range(1, k):
            while i:
                if i % 2:
                    root = i // 2
                else:
                    root = i // 2 - 1
                if heap[root] > heap[i]:
                    heap[root], heap[i] = heap[i], heap[root]
                i = root
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                index = 0
                left_index = index * 2 + 1
                right_index = left_index + 1
                while left_index <= k - 1:
                    min_index = index
                    if heap[left_index] < heap[min_index]:
                        min_index = left_index
                    if right_index <= k - 1 and heap[right_index] < heap[min_index]:
                        min_index = right_index
                    if min_index == index:
                        break
                    heap[min_index], heap[index] = heap[index], heap[min_index]
                    index = min_index
                    left_index = index * 2 + 1
                    right_index = left_index + 1
        return heap[0]
# @lc code=end

