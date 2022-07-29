/*
 * @lc app=leetcode id=350 lang=cpp
 *
 * [350] Intersection of Two Arrays II
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>
using std::cout;
using std::endl;
using std::min;
using std::vector;

const int MAXLENGTH = 1001;
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        int nums1Count[MAXLENGTH] = {0};
        int nums2Count[MAXLENGTH] = {0};
        for (vector<int>::iterator itr = nums1.begin(); itr != nums1.end(); ++itr)
            ++nums1Count[*itr];
        for (vector<int>::iterator itr = nums2.begin(); itr != nums2.end(); ++itr)
            ++nums2Count[*itr];
        for (int i = 0; i != MAXLENGTH; ++i) {
            int count = min(nums1Count[i], nums2Count[i]);
            for (int j = 0; j != count; ++j)
                res.push_back(i);
        }
        return res;
    }
};

//int main() {
//    vector<int> a {4,9,5};
//    vector<int> b {9,4,9,8,4};
//    Solution s = Solution();
//    auto res = s.intersect(a, b);
//    for (auto itr = res.begin(); itr != res.end(); ++itr)
//        cout << *itr << " ";
//    cout << endl;
//}
// @lc code=end

