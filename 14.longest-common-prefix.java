/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (34.94%)
 * Likes:    2271
 * Dislikes: 1758
 * Total Accepted:    697K
 * Total Submissions: 2M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 * Example 1:
 *
 *
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 *
 *
 * Example 2:
 *
 *
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 *
 * Note:
 *
 * All given inputs are in lowercase letters a-z.
 *
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        int minLength = strs[0].length();
        for (String s : strs)
            minLength = Math.min(minLength, s.length());
        int i = 0;
        String prefix = "";
        while (i < minLength) {
            char c = '\0';
            boolean isBreak = false;
            for (String s : strs) {
                if (c == '\0')
                    c = s.charAt(i);
                else if (c != s.charAt(i)) {
                    isBreak = true;
                    break;
                }
            }
            if (!isBreak)
                prefix += c;
            else
                break;
            i++;
        }
        return prefix;
    }
}
// @lc code=end

