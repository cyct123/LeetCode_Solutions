/*
 * @lc app=leetcode id=454 lang=cpp
 *
 * [454] 4Sum II
 */

// @lc code=start
#include <unordered_map>
#include <vector>
using std::vector;
using std::unordered_map;
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> records;
        int count = 0;
        for (vector<int>::iterator itr1 = nums1.begin(); itr1 != nums1.end(); ++itr1)
            for (vector<int>::iterator itr2 = nums2.begin(); itr2 != nums2.end(); ++itr2)
                ++records[-*itr1 - *itr2];
        for (vector<int>::iterator itr3 = nums3.begin(); itr3 != nums3.end(); ++itr3)
            for (vector<int>::iterator itr4 = nums4.begin(); itr4 != nums4.end(); ++itr4)
                    count += records[*itr3 + *itr4];
        return count;
    }
};
// @lc code=end

