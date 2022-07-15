/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

// @lc code=start
//#include <string>
//#include <iostream>
//using std::endl;
//using std::cout;
//using std::string;
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return s.substr(0, backspaceHelper(s)) == t.substr(0, backspaceHelper(t));
    }
    int backspaceHelper(string& s) {
        int slowIndex = 0;
        for (int fastIndex = 0; fastIndex != s.size(); ++fastIndex) {
            if (s[fastIndex] == '#') {
                if (slowIndex > 0) --slowIndex;
            } else {
                s[slowIndex++] = s[fastIndex];
            }

        }
        return slowIndex;
    }
};

//int main() {
//    string s = "ab##";
//    string t = "c#d#";
//    Solution S = Solution();
//    int sLen = S.backspaceHelper(s);
//    cout << s << " " << s.substr(0, sLen) << endl;
//    int tLen = S.backspaceHelper(t);
//    cout << t << " " << s.substr(0, tLen) << endl;
//    return 0;
//}
// @lc code=end

