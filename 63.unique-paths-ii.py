#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.92%)
# Likes:    1300
# Dislikes: 213
# Total Accepted:    259.4K
# Total Submissions: 764.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        dp = [0] * m * n
        for i in range(m * n):
            row = i // n
            col = i - row * n
            if obstacleGrid[row][col]:
                continue
            if row == 0 and col == 0:
                dp[i] = 1
            if row >= 1:
                idx = (row - 1) * n + col
                dp[i] += dp[idx]
            if col >= 1:
                idx = row * n + col - 1
                dp[i] += dp[idx]
        return dp[-1]

# @lc code=end

