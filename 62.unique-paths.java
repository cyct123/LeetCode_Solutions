import java.util.ArrayList;

/*
 * @lc app=leetcode id=62 lang=java
 *
 * [62] Unique Paths
 *
 * https://leetcode.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (51.10%)
 * Likes:    2439
 * Dislikes: 175
 * Total Accepted:    397.1K
 * Total Submissions: 773.3K
 * Testcase Example:  '3\n2'
 *
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in
 * the diagram below).
 *
 * The robot can only move either down or right at any point in time. The robot
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in
 * the diagram below).
 *
 * How many possible unique paths are there?
 *
 *
 * Above is a 7 x 3 grid. How many possible unique paths are there?
 *
 * Note: m and n will be at most 100.
 *
 * Example 1:
 *
 *
 * Input: m = 3, n = 2
 * Output: 3
 * Explanation:
 * From the top-left corner, there are a total of 3 ways to reach the
 * bottom-right corner:
 * 1. Right -> Right -> Down
 * 2. Right -> Down -> Right
 * 3. Down -> Right -> Right
 *
 *
 * Example 2:
 *
 *
 * Input: m = 7, n = 3
 * Output: 28
 *
 */

// @lc code=start
class Solution {
    public int uniquePaths(int m, int n) {
        int length = m * n;
        int[] dp = new int[length];
        for (int i = 0; i < length; i++) {
            if (i == 0)
                dp[i] = 1;
            else if (i < m)
                dp[i] = dp[i-1];
            else if (i % m == 0)
                dp[i] = dp[i-m];
            else {
                dp[i] = dp[i-1] + dp[i-m];
            }
        }
        return dp[length -1];
    }
}
// @lc code=end

