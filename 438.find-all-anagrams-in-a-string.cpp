/*
 * @lc app=leetcode id=438 lang=cpp
 *
 * [438] Find All Anagrams in a String
 */

// @lc code=start
#include <vector>
#include <string>
using std::vector;
using std::string;
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        if (p.size() > s.size()) return res;
        int pRecord[26] = {0};
        for (string::iterator itr = p.begin(); itr != p.end(); ++itr)
            ++pRecord[*itr - 'a'];
        int sRecord[26] = {0};
        for (int i = 0; i != s.size() - p.size() + 1; ++i) {
            if (!i)
                for (int j = 0; j != p.size(); ++j)
                    ++sRecord[s[i+j] - 'a'];
            else {
                --sRecord[s[i-1] - 'a'];
                ++sRecord[s[i+p.size() - 1] - 'a'];
            }
            if (isSameArray(pRecord, sRecord))
                res.push_back(i);
        }
        return res;
    }
private:
    bool isSameArray(int a[] , int b[]) {
        for(int i = 0; i != 26; ++i)
            if (a[i] != b[i]) return false;
        return true;
    }
};
// @lc code=end

