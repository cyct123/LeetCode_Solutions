#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (44.79%)
# Likes:    8567
# Dislikes: 180
# Total Accepted:    567.7K
# Total Submissions: 1.3M
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
#
# Example 1:
#
#
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
#
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxLength = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                maxLength = dp[i][j] if dp[i][j] > maxLength else maxLength
        return maxLength * maxLength


# @lc code=end
if __name__ == "__main__":
    matrix = [["0", "1"], ["1", "0"]]
    print(Solution().maximalSquare(matrix))
