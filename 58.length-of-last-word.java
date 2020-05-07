/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (32.44%)
 * Likes:    523
 * Dislikes: 2096
 * Total Accepted:    333.2K
 * Total Submissions: 1M
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word (last word means the last
 * appearing word if we loop from left to right) in the string.
 *
 * If the last word does not exist, return 0.
 *
 * Note: A word is defined as a maximal substring consisting of non-space
 * characters only.
 *
 * Example:
 *
 *
 * Input: "Hello World"
 * Output: 5
 *
 *
 *
 *
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        int len = 0;
        int prevLen = 0;
        char prevChar = '\0';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') {
                if (prevChar == c)
                    continue;
                else {
                    prevLen = len;
                    len = 0;
                }
            }
            else
                len++;
            prevChar = c;
        }
        return (len == 0) ? prevLen: len;
    }
}
// @lc code=end

