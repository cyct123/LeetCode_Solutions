/*
 * @lc app=leetcode id=977 lang=cpp
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
//#include <vector>
//#include <cmath>
//#include <iostream>
//#include <algorithm>
//using std::reverse;
//using std::cout;
//using std::endl;
//using std::abs;
//using std::vector;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> squareNums;
        int left = 0;
        int right = nums.size() - 1;
        while (left != right) {
            if (abs(nums[left]) >= abs(nums[right])) {
                squareNums.push_back(nums[left] * nums[left]);
                ++left;
            } else {
                squareNums.push_back(nums[right] * nums[right]);
                --right;
            }
        }
        squareNums.push_back(nums[left] * nums[left]);
        reverse(squareNums.begin(), squareNums.end());
        return squareNums;
    }
};


//int main() {
//    vector<int> nums{1};
//    Solution s = Solution();
//    vector<int> ret = s.sortedSquares(nums);
//    for (auto itr = ret.begin(); itr != ret.end(); ++itr)
//        cout << *itr << endl;
//    return 0;
//}
// @lc code=end

