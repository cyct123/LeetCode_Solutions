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
        for (int i = 0; i < s.size(); i += (2 * k)) {
            if (i + k < s.size())
                reverse(s, i, i + k);
            else
                reverse(s, i, s.size());
        }
        return s;
    }
private:
    void reverse(string& s, int begin, int end){
        for (int i = begin, j = end - 1; i < j; ++i, --j)
            swap(s[i], s[j]);
    }
};
// @lc code=end

