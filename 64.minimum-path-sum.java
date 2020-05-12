import java.util.Arrays;

/*
 * @lc app=leetcode id=64 lang=java
 *
 * [64] Minimum Path Sum
 *
 * https://leetcode.com/problems/minimum-path-sum/description/
 *
 * algorithms
 * Medium (50.70%)
 * Likes:    2139
 * Dislikes: 48
 * Total Accepted:    312.6K
 * Total Submissions: 613.6K
 * Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
 *
 * Given a m x n grid filled with non-negative numbers, find a path from top
 * left to bottom right which minimizes the sum of all numbers along its path.
 *
 * Note: You can only move either down or right at any point in time.
 *
 * Example:
 *
 *
 * Input:
 * [
 * [1,3,1],
 * ⁠ [1,5,1],
 * ⁠ [4,2,1]
 * ]
 * Output: 7
 * Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 *
 *
 */

// @lc code=start
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        int length = m * n;
        int[] dp = new int[length];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int index = i + j * m;
                if (index == 0)
                    dp[index] = grid[i][j];
                else if (index < m)
                    dp[index] = grid[i][j] + dp[index-1];
                else if (index % m == 0)
                    dp[index] = grid[i][j] + dp[index-m];
                else
                    dp[index] = grid[i][j] + (dp[index-1] < dp[index-m] ? dp[index-1] : dp[index-m]);
            }
        }
        return dp[length-1];
    }
}
// @lc code=end

