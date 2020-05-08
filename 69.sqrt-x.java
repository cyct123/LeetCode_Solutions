/*
 * @lc app=leetcode id=69 lang=java
 *
 * [69] Sqrt(x)
 *
 * https://leetcode.com/problems/sqrtx/description/
 *
 * algorithms
 * Easy (32.80%)
 * Likes:    1056
 * Dislikes: 1689
 * Total Accepted:    479K
 * Total Submissions: 1.5M
 * Testcase Example:  '4'
 *
 * Implement int sqrt(int x).
 *
 * Compute and return the square root of x, where x is guaranteed to be a
 * non-negative integer.
 *
 * Since the return type is an integer, the decimal digits are truncated and
 * only the integer part of the result is returned.
 *
 * Example 1:
 *
 *
 * Input: 4
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since
 * the decimal part is truncated, 2 is returned.
 *
 *
 */

// @lc code=start
class Solution {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;
        int i = 1;
        int j = x;
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (mid == x / mid)
                return mid;
            else if (mid < x / mid)
                i = mid + 1;
            else
                j = mid - 1;
        }
        return (i > j) ? j: i;
    }
}
// @lc code=end

