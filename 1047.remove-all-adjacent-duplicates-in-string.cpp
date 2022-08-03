/*
 * @lc app=leetcode id=1047 lang=cpp
 *
 * [1047] Remove All Adjacent Duplicates In String
 */

// @lc code=start
#include <vector>
#include <string>
using std::vector;
using std::string;
class Solution {
public:
    string removeDuplicates(string s) {
        vector<char> chars;
        for (string::iterator itr = s.begin(); itr != s.end(); ++itr) {
            if (!chars.empty() && *itr == chars.back())
                chars.pop_back();
            else
                chars.push_back(*itr);
        }
        string res(chars.begin(), chars.end());
        return res;
    }
};
// @lc code=end

