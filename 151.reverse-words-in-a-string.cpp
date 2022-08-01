/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
#include <string>
#include <algorithm>
#include <iostream>
using std::cout;
using std::endl;
using std::string;
using std::reverse;


class Solution {
public:
    string reverseWords(string s) {
        removeExtraSpace(s);
        reverseString(s);
        reverseWord(s);
        return s;
    }
private:
    void removeExtraSpace(string& s) {
        int wordBegin = -1;
        int newIndex = 0;
        for (int i = 0; i != s.size(); ++i) {
            if(s[i] != ' ') {
                if (wordBegin == -1)
                    wordBegin = i;
            }
            else {
                if (wordBegin != -1) {
                    for (int j = 0; j != i - wordBegin; ++j)
                        s[newIndex+j] = s[wordBegin+j];
                    s[newIndex + i - wordBegin] = ' ';
                    newIndex = newIndex + i - wordBegin + 1;
                    wordBegin = -1;
                }
            }
        }
        if (wordBegin != -1) {
            for (int j = 0; j != s.size() - wordBegin; ++j)
                s[newIndex+j] = s[wordBegin+j];
            newIndex = newIndex + s.size() - wordBegin + 1;
        }
        s.erase(s.begin() + newIndex - 1, s.end());
    }
    
    void reverseString(string& s){
        reverse(s.begin(), s.end()); 
    }

    void reverseWord(string& s){
        int begin = 0;
        for(int i = 0; i != s.size(); ++i) {
            if (s[i] == ' ') {
                reverse(s.begin() + begin, s.begin() + i);
                begin = i + 1;
            }
        }
        reverse(s.begin() + begin, s.end());
    }
};

//int main() {
//    string s = "  hello world  ";
//    Solution so = Solution();
//    cout << so.reverseWords(s) << endl; 
//}
// @lc code=end

