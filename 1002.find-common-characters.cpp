/*
 * @lc app=leetcode id=1002 lang=cpp
 *
 * [1002] Find Common Characters
 */

// @lc code=start
#include <vector>
#include <string>
using std::string;
using std::vector;


const int AlPHABETLENGTH = 26;
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> resRecord(AlPHABETLENGTH, 0);
        for (vector<string>::iterator strItr = words.begin(); strItr != words.end(); ++strItr){
            if (strItr == words.begin())
                for (string::iterator charItr = strItr->begin(); charItr != strItr->end(); ++charItr)
                    ++resRecord[*charItr - 'a'];
            else {
                vector<int> charRecord(AlPHABETLENGTH, 0); 
                for (string::iterator charItr = strItr->begin(); charItr != strItr->end(); ++charItr)
                    ++charRecord[*charItr - 'a'];
                resRecord = findCommonRecords(resRecord, charRecord);
            }
        }
        vector<string> res;
        for (int i = 0; i != AlPHABETLENGTH; ++i)
            for (int j = resRecord[i]; j != 0; --j)
                res.push_back(string(1, 'a' + i));
        return res;
    }
private:
    vector<int> findCommonRecords(vector<int>& a, vector<int>& b) {
        for (int i = 0; i != AlPHABETLENGTH; ++i) {
            if (a[i] > b[i])
                a[i] = b[i];
        }
        return a;
    }
};
// @lc code=end

