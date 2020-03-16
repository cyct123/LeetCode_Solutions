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

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        for i in range(k):
            while i:
                if i % 2 == 0:
                    root = i // 2 - 1
                else:
                    root = i // 2
                if heap[i] < heap[root]:
                    heap[i], heap[root] = heap[root], heap[i]
                i = root
        for i in range(k, len(nums)):
            num = nums[i]
            if num > heap[0]:
                heap[0] = num
                start = 0
                while start < k // 2:
                    left = 2 * start + 1
                    right = 2 * (start + 1)
                    if right >= k or heap[left] <= heap[right]:
                        if heap[start] > heap[left]:
                            heap[start], heap[left] = heap[left], heap[start]
                            start = left
                            continue
                        else:
                            break
                    if right >= k or heap[left] > heap[right]:
                        if heap[start] > heap[right]:
                            heap[start], heap[right] = heap[right], heap[start]
                            start = right
                            continue
                        else:
                            break
        return heap[0]



# @lc code=end

