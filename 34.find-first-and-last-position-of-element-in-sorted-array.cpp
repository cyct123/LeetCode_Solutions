/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
#include <vector>
using std::vector;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if(nums[mid] == target){
                int leftIndex = mid;
                int rightIndex = mid;
                for(;leftIndex >= 0 && nums[leftIndex]==target; --leftIndex);
                for(;rightIndex <= nums.size() - 1 && nums[rightIndex]==target; ++rightIndex);
                return {++leftIndex, --rightIndex};
            }
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return {-1, -1};
    }
};
// @lc code=end

