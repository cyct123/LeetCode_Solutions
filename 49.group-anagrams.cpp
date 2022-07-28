/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
 */

// @lc code=start
//#include <vector>
//#include <string>
//#include <unordered_map>
//#include <iostream>
//using std::unordered_map;
//using std::string;
//using std::vector;
class Solution {
public:
    vector<vector<string> > groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > strMap;
        for (vector<string>::iterator itr = strs.begin(); itr != strs.end(); ++itr) {
            strMap[strSort(*itr)].push_back(*itr);
        }
        vector<vector<string> > res;
        for (const auto& n: strMap)
            res.push_back(n.second);
        return res;
    }
private:
    string strSort(string& str) {
        int record[26] = {0};
        for(string::iterator itr = str.begin(); itr != str.end(); ++itr)
            ++record[*itr - 'a'];
        string res;
        for (int i = 0; i != 26; ++i)
            res += string(record[i], i + 'a');
        return res;
    }
};

//int main() {
//    vector<string> strs{"eat", "tea", "tan", "ate", "nat", "bat"};
//    Solution s = Solution();
//    auto ret = s.groupAnagrams(strs);
//    for (vector<vector<string> >::iterator itr = ret.begin(); itr != ret.end(); ++itr) {
//        for (vector<string>:: iterator strItr = itr->begin(); strItr != itr->end(); ++strItr) {
//            std::cout << *strItr << " ";
//        } 
//        std::cout << std::endl;
//    }
//}
// @lc code=end

