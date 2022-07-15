/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
//#include <vector>
//using std::vector;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        int slowIndex = 0;
        int prevNum = nums[slowIndex];
        for(int fastIndex = slowIndex + 1; fastIndex != nums.size(); ++fastIndex) {
            if (nums[fastIndex] != prevNum) {
                nums[++slowIndex] = nums[fastIndex];
                prevNum = nums[fastIndex];
            }
        }
        return slowIndex + 1;
    }
};
// @lc code=end

