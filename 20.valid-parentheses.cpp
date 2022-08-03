/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
#include <string>
#include <vector>
#include <unordered_map>
using std::unordered_map;
using std::string;
using std::vector;
class Solution {
public:
    bool isValid(string s) {
        vector<char> pars;
        unordered_map<char, char> parMap = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        for (string::iterator itr = s.begin(); itr != s.end(); ++itr) {
            if (parMap.count(*itr)) {
                if (pars.empty()) return false;
                char par = pars.back();
                pars.pop_back();
                if (par != parMap[*itr])
                    return false;
            } else
                pars.push_back(*itr);
        }
        return pars.empty();
    }
};
// @lc code=end

