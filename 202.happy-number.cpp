/*
 * @lc app=leetcode id=202 lang=cpp
 *
 * [202] Happy Number
 */

// @lc code=start
#include <unordered_set>
using std::unordered_set; 
class Solution {
public:
    bool isHappy(int n) {
        int ret = n;
        unordered_set<int> calcValues;
        while (!calcValues.count(ret)) {
            calcValues.insert(ret);
            ret = sumSquare(ret);
            if (ret == 1) return true;
       }
        return false;
    }

private:
    int sumSquare(int n) {
        int sum = 0;
        while (n) {
            int reminder = n % 10;
            sum += reminder * reminder;
            n /= 10;
        }
        return sum;
    }
};
// @lc code=end

