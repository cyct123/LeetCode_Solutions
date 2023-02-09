/*
 * @lc app=leetcode id=704 lang=cpp
 *
 * [704] Binary Search
 */
#include <vector>
using std::vector;

// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        while (high >= low){
            int mid = low + (high - low) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return -1;
    }
};
// @lc code=end

