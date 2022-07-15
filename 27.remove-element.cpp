/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
//#include <vector>
//#include <iostream>
//using std::endl;
//using std::cout;
//using std::vector;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty())
            return 0;
        int left = 0;
        int right = nums.size() - 1;
        for(; right >= 0 && nums[right] == val; --right);
        while (left <= right) {
            if(nums[left] == val) {
                int tmp = nums[right];
                nums[right] = nums[left];
                nums[left] = tmp;
                for(; right >= 0 && nums[right] == val; --right);
            }
            ++left;
        }
        return left; 
    }
};

//int main() {
//    vector<int> nums{0};
//    int val = 1;
//    Solution s = Solution();
//    cout << s.removeElement(nums, val) << endl;
//    return 0; 
//}
// @lc code=end

