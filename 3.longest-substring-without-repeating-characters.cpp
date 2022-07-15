/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
//#include <string>
//#include <set>
//#include <iostream>
//using std::string;
//using std::set;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() <= 1) return s.size();
        int ret = 0;
        int leftIndex = 0;
        set<char> chSet;
        for (int rightIndex = 0; rightIndex != s.size(); ++rightIndex) {
            char ch = s[rightIndex];
            if (!chSet.count(ch)) {
                int length = rightIndex - leftIndex + 1;
                ret = ret < length? length: ret; 
            } else {
                while (s[leftIndex] != ch){
                    chSet.erase(s[leftIndex++]);
                }
                chSet.erase(s[leftIndex++]);
            }
            chSet.insert(ch);
        }
        return ret;
    }
};

//void PrintRet(string s, Solution S) {
//    std::cout << s << " " << S.lengthOfLongestSubstring(s) << std::endl;
//}
//
//int main() {
//    string s1 = "pwwkew";
//    string s2 = "dvdf";
//    string s3 = "bbbbb";
//    string s4 = "abcabcbb";
//    Solution S = Solution();
//    PrintRet(s1, S);
//    PrintRet(s2, S);
//    PrintRet(s3, S);
//    PrintRet(s4, S);
//}
// @lc code=end

