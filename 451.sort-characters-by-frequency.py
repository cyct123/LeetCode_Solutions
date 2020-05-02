#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (58.59%)
# Likes:    1183
# Dislikes: 95
# Total Accepted:    138.4K
# Total Submissions: 232.2K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            count = freq.get(c, 0)
            count += 1
            freq[c] = count
        sortedChars = sorted(freq, key=freq.get, reverse=True)
        result = ""
        for count in sortedChars:
            result += count * (freq[count])
        return result
# @lc code=end

