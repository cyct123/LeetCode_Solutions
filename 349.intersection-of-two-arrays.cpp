/*
 * @lc app=leetcode id=349 lang=cpp
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
#include <unordered_set>
#include <vector>
using std::unordered_set;
using std::vector;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> res;
        unordered_set<int> numSet(nums1.begin(), nums1.end()); 
        for (vector<int>::iterator itr = nums2.begin(); itr != nums2.end(); ++itr)
            if (numSet.find(*itr) != numSet.end())
                res.insert(*itr);
    return vector<int>(res.begin(), res.end());
    }
};
// @lc code=end

