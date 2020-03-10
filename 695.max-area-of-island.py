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

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                curArea = 0
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()
                    if not grid[row][col]:
                        continue
                    grid[row][col] = 0
                    curArea += 1
                    if row > 0 and grid[row-1][col] == 1:
                        stack.append((row-1, col))
                    if col > 0 and grid[row][col-1] == 1:
                        stack.append((row, col-1))
                    if row < m - 1 and grid[row+1][col] == 1:
                        stack.append((row+1, col))
                    if col < n - 1 and grid[row][col+1] == 1:
                        stack.append((row, col+1))
                    maxArea = max(maxArea, curArea)
        return maxArea

# @lc code=end

