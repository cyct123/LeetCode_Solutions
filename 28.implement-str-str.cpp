/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Implement strStr()
 */

// @lc code=start
#include <string>
using std::string;
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (!needle.size()) return 0;
        if (haystack.size() < needle.size()) return -1;
        for (int i = 0; i != haystack.size() - needle.size() + 1; ++i) {
            if (isSameString(haystack, needle, i))
                return i;
        }
        return -1;
    } 
private:
    bool isSameString(string& haystack, string& needle, int offset){
        for(int i = 0; i != needle.size(); ++i)
            if (haystack[i+offset] != needle[i])
                return false;
        return true;
    }
};
// @lc code=end

