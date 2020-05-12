import java.util.Arrays;

import org.graalvm.compiler.hotspot.phases.OnStackReplacementPhase;

/*
 * @lc app=leetcode id=63 lang=java
 *
 * [63] Unique Paths II
 *
 * https://leetcode.com/problems/unique-paths-ii/description/
 *
 * algorithms
 * Medium (33.92%)
 * Likes:    1300
 * Dislikes: 213
 * Total Accepted:    259.4K
 * Total Submissions: 764.3K
 * Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
 *
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in
 * the diagram below).
 *
 * The robot can only move either down or right at any point in time. The robot
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in
 * the diagram below).
 *
 * Now consider if some obstacles are added to the grids. How many unique paths
 * would there be?
 *
 *
 *
 * An obstacle and empty space is marked as 1 and 0 respectively in the grid.
 *
 * Note: m and n will be at most 100.
 *
 * Example 1:
 *
 *
 * Input:
 * [
 * [0,0,0],
 * [0,1,0],
 * [0,0,0]
 * ]
 * Output: 2
 * Explanation:
 * There is one obstacle in the middle of the 3x3 grid above.
 * There are two ways to reach the bottom-right corner:
 * 1. Right -> Right -> Down -> Down
 * 2. Down -> Down -> Right -> Right
 *
 *
 */

// @lc code=start
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0)
            return 0;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int length = m * n;
        int[] dp = new int[length];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int index = i + j * m;
                if (index == 0)
                    dp[index] = (obstacleGrid[i][j] == 1) ? 0 : 1;
                else {
                    int leftDp = (i == 0) ? 0: dp[index-1];
                    int aboveDP = (j == 0) ? 0: dp[index-m];
                    dp[index] = (obstacleGrid[i][j] == 1) ? 0: (aboveDP + leftDp);
                }
            }
        }
        return dp[length-1];
    }
}
// @lc code=end

