/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numberMap;
        for (int i = 0; i < nums.size(); ++i) {
            auto itr = numberMap.find(target - nums[i]);
            if (itr != numberMap.end())
                return vector<int> {itr->second, i};
            numberMap[nums[i]] = i;
        }
        return {};
    }
};
// @lc code=end

