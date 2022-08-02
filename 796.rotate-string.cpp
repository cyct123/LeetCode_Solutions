/*
 * @lc app=leetcode id=796 lang=cpp
 *
 * [796] Rotate String
 */

// @lc code=start
#include <string>
using std::string;
class Solution {
public:
    bool rotateString(string s, string goal) {
        for (int i = 0; i != s.size(); ++i) {
            if (rotateString(s, goal, i))
                return true;
        }
        return false;  
    }
private:
    bool rotateString(string& s, string& goal, int offset){\
        for (int i = 0; i != s.size(); ++i) {
            int newIndex = (i + offset) % s.size();
            if (s[newIndex] != goal[i])
                return false; 
        }
        return true;
    }
};
// @lc code=end

