import java.util.Arrays;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (32.90%)
 * Likes:    1671
 * Dislikes: 306
 * Total Accepted:    311.9K
 * Total Submissions: 947.9K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 *
 * Note:
 *
 * The solution set must not contain duplicate quadruplets.
 *
 * Example:
 *
 *
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 *
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 *
 *
 */

// @lc code=start
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        int i = 0;
        while (i < nums.length - 3) {
            int j = i + 1;
            while (j < nums.length - 2) {
                int k = j + 1;
                int l = nums.length - 1;
                while (k < l) {
                    int sum = nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
                        while (k < nums.length - 1 && nums[k] == nums[k+1])
                            k++;
                        while (l > j + 1 && nums[l] == nums[l-1])
                            l--;
                        k++;
                        l--;
                    } else if (sum < target) {
                        k++;
                    } else if (sum > target) {
                        l--;
                    }
                }
                j++;
                while (j < nums.length - 2 && nums[j-1] == nums[j])
                    j++;
            }
            i++;
            while (i < nums.length - 3 && nums[i-1] == nums[i])
                i++;
        }
        return res;
    }
}
// @lc code=end

