/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>
using std::sort;
using std::vector;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());
        int i = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i-1] == nums[i]) continue;
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                if (!(nums[i] + nums[left] + nums[right])) {
                    res.push_back({nums[i], nums[left], nums[right]});
                    while ((left < right) && (nums[left+1] == nums[left])) ++left;
                    while ((right > 1) && (nums[right-1] == nums[right])) --right;
                    ++left;
                    --right;
                } else if (nums[i] + nums[left] + nums[right] > 0) 
                    --right;
                else
                    ++left;
            }
        }
        return res;
    }
};
// @lc code=end

