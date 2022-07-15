/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
//#include <vector>
//using std::vector;
const int MAXLENGTH = 100001;
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int leftIndex = 0;
        int sum = 0;
        int ret = MAXLENGTH;
        for (int rightIndex = 0; rightIndex != nums.size(); ++rightIndex) {
            sum += nums[rightIndex];
            while (sum >= target) {
                int length = rightIndex - leftIndex + 1;
                ret = ret < length? ret: length;
                sum -= nums[leftIndex++];
            }
        } 
        return ret == MAXLENGTH ? 0: ret;
    }
};
// @lc code=end

