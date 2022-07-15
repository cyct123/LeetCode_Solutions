/*
 * @lc app=leetcode id=367 lang=cpp
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num == 1)
            return true;
        int left = 0;
        int right = num;
        while(left <= right){
            int mid = left + ((right - left) >> 1);
            if (mid == num / mid){
                if (mid * mid == num)
                    return true;
                else
                    return false;
            }
            if (mid < num / mid)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return false;
    }
};
// @lc code=end

