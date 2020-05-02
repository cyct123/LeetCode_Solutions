import java.lang.reflect.Array;
import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (45.06%)
 * Likes:    13572
 * Dislikes: 494
 * Total Accepted:    2.6M
 * Total Submissions: 5.7M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 *
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 *
 * Example:
 *
 *
 * Given nums = [2, 7, 11, 15], target = 9,
 *
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 *
 *
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> map = new HashMap<>();
       for (int i = 0; i < nums.length; i++) {
           int diff = target - nums[i];
           if (map.containsKey(diff)) {
               return new int[] {map.get(diff), i};
           }
           map.put(nums[i], i);
       }
       throw new IllegalArgumentException("No solution");
    }
}
// @lc code=end

