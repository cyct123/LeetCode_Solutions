/*
 * @lc app=leetcode id=283 lang=cpp
 *
 * [283] Move Zeroes
 */

// @lc code=start
//#include <vector>
//using std::vector;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.size() <= 1) return;
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex != nums.size(); ++fastIndex) {
            if (nums[fastIndex] != 0) {
                if (slowIndex != fastIndex) {
                    int tmp = nums[slowIndex];
                    nums[slowIndex] = nums[fastIndex];
                    nums[fastIndex] = tmp; 
                }
                ++slowIndex;
            }
        }
    }
};
// @lc code=end

