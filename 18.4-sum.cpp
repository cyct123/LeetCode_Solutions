/*
 * @lc app=leetcode id=18 lang=cpp
 *
 * [18] 4Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>
using std::cout;
using std::endl;
using std::vector;
using std::sort;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target) {
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0 && target <= 0) break;
            if (i > 0 && nums[i-1] == nums[i]) continue;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] > 0 && target <= 0) break;
                if (j > i + 1 && nums[j-1] == nums[j]) continue;
                int left = j + 1;
                int right = nums.size() - 1;
                while (left < right) {
                    if (nums[i] + nums[j] == target - nums[left] - nums[right]) {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while ((left < right) && (nums[left+1] == nums[left])) ++left;
                        while ((left < right) && (nums[right-1] == nums[right])) --right;
                        ++left;
                        --right;
                    } else if (nums[i] + nums[j] > target - nums[left] - nums[right])
                        --right;
                    else
                        ++left;
                }
            }
        }
        return res;
    }
};

//void PrintRes(vector<vector<int> >& res) {
//    for (vector<vector<int> >::iterator resItr = res.begin(); resItr != res.end(); ++resItr)
//        for (vector<int>::iterator numItr = resItr->begin(); numItr != resItr->end(); ++numItr)
//            cout << *numItr << " ";
//        cout << endl;        
//}
//
//
//int main() {
//    vector<int> nums{2,2,2,2,2};
//    Solution s = Solution();
//    auto res = s.fourSum(nums, 8);
//    PrintRes(res);
//}
// @lc code=end

