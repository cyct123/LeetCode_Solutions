/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
 */

// @lc code=start
//#include <string>
//using std::string;
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int record[26] = {0};
        for (string::iterator itr = magazine.begin(); itr != magazine.end(); ++itr)
            ++record[*itr - 'a'];
        for (string::iterator itr = ransomNote.begin(); itr != ransomNote.end(); ++itr) {
            if (!record[*itr - 'a']) return false;
            --record[*itr - 'a'];
        }
        return true;
    }
};
// @lc code=end

