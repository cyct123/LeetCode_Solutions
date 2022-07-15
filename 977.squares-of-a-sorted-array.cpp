/*
 * @lc app=leetcode id=977 lang=cpp
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
//#include <vector>
//#include <iostream>
//using std::cout;
//using std::endl;
//using std::vector;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> squareNums(nums.size(), 0);
        int left = 0;
        int right = nums.size() - 1;
        int index = nums.size() - 1;
        while (left != right) {
            int leftSquare = nums[left] * nums[left];
            int rightSquare = nums[right] * nums[right];
            if (leftSquare >= rightSquare) {
                squareNums[index] = leftSquare;
                ++left;
            } else {
                squareNums[index] = rightSquare;
                --right;
            }
            --index;
        }
        squareNums[index] = nums[left] * nums[left];
        return squareNums;
    }
};


//int main() {
//    vector<int> nums{-7,-3,2,3,11};
//    Solution s = Solution();
//    vector<int> ret = s.sortedSquares(nums);
//    for (auto itr = ret.begin(); itr != ret.end(); ++itr)
//        cout << *itr << endl;
//    return 0;
//}
// @lc code=end

