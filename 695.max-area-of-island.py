#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (60.34%)
# Likes:    1532
# Dislikes: 69
# Total Accepted:    126.2K
# Total Submissions: 208.2K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
#
# Example 1:
#
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
#
# Example 2:
#
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
#
# Note: The length of each dimension in the given grid does not exceed 50.
#
#
from typing import List


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, self.dfsArea(grid, i, j))
        return maxArea

    def dfsArea(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or not grid[i][j]:
            return 0
        grid[i][j] = 0
        return (
            1
            + self.dfsArea(grid, i - 1, j)
            + self.dfsArea(grid, i, j - 1)
            + self.dfsArea(grid, i + 1, j)
            + self.dfsArea(grid, i, j + 1)
        )


# @lc code=end
