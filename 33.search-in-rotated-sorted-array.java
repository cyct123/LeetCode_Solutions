/*
 * @lc app=leetcode id=33 lang=java
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (33.59%)
 * Likes:    3801
 * Dislikes: 405
 * Total Accepted:    580.6K
 * Total Submissions: 1.7M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 *
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 *
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 *
 * You may assume no duplicate exists in the array.
 *
 * Your algorithm's runtime complexity must be in the order of O(log n).
 *
 * Example 1:
 *
 *
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 *
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;
        if (j < 0)
            return -1;
        boolean isLeft = true;
        if (nums[j] >= target)
            isLeft = false;
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (isLeft == true) {
                if (nums[mid] < nums[0] || nums[mid] > target)
                    j = mid - 1;
                else if (nums[mid] == target)
                    return mid;
                else if (nums[mid] < target)
                    i = mid + 1;
            } else {
                if (nums[mid] > nums[nums.length-1] || nums[mid] < target)
                    i = mid + 1;
                else if (nums[mid] == target)
                    return mid;
                else if (nums[mid] > target)
                    j = mid - 1;
            }
        }
        return -1;
    }
}
// @lc code=end

