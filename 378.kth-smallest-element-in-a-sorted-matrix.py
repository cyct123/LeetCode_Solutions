#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (52.05%)
# Likes:    1980
# Dislikes: 114
# Total Accepted:    167.2K
# Total Submissions: 315.9K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        for l in matrix:
            hq.extend(l)
        return heapq.nsmallest(k, hq)[-1]
# @lc code=end

