/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
#include <string>
#include <vector>
#include <iostream>
using std::string;
using std::vector;
class Solution {
public:
    bool isValid(string s) {
        vector<char> pars;
        string leftPar = "([{";
        string rightPar = ")]}";
        for (string::iterator itr = s.begin(); itr != s.end(); ++itr) {
            if (leftPar.find( *itr) != string::npos)
                pars.push_back( *itr);
            else {
                if (pars.empty()) return false;
                char par = pars.back();
                pars.pop_back();
                if (leftPar.find(par) != rightPar.find( *itr))
                    return false;
            }
        }
        return pars.empty();
    }
};

//int main() {
//    string s = "()";
//    Solution so = Solution();
//    std::cout << so.isValid(s) << std::endl;
//    string test = "([{";
//    std::cout << test.find('(') << std::endl;
//    return 0;
//}
// @lc code=end

