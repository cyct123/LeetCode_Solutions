#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (50.70%)
# Likes:    2139
# Dislikes: 48
# Total Accepted:    312.6K
# Total Submissions: 613.6K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        dp = [0] * m * n
        for i in range(m * n):
            row = i // n
            col = i - row * n
            if row == 0 and col == 0:
                dp[i] = grid[row][col]
                continue
            if row >= 1:
                idx = (row - 1) * n + col
                upDp = dp[idx]
            else:
                upDp = float('Inf')
            if col >= 1:
                idx = row * n + col -1
                leftDp = dp[idx]
            else:
                leftDp = float('Inf')
            dp[i] = min(leftDp, upDp) + grid[row][col]
        return dp[-1]


# @lc code=end

