/*
 * @lc app=leetcode id=541 lang=cpp
 *
 * [541] Reverse String II
 */

// @lc code=start
#include <string>
#include <algorithm>
using std::string;
using std::swap;


class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.size() / k + 1; ++i) {
            if (!(i % 2)) {
                int left = i * k;
                int right = s.size() > (i + 1) * k ? (i + 1) * k - 1: s.size() - 1;
                while (left < right) {
                    swap(s[left], s[right]);
                    ++left;
                    --right;
                }
            }
        }
        return s;
    }
};
// @lc code=end

