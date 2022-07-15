/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1)
            return x;
        int left = 0;
        int right = x;
        while(left <= right) {
            int mid = left + ((right - left) >> 1);
            if (mid == x / mid)
                return mid;
            if (mid < x / mid)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return right;
    }
};
// @lc code=end

