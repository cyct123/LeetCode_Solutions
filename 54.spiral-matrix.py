#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (42.01%)
# Likes:    7913
# Dislikes: 871
# Total Accepted:    785.5K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#

from typing import List


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        rowLength = len(matrix)
        colLength = len(matrix[0])
        loop = (min(rowLength, colLength) + 1) // 2
        for i in range(loop):
            rowStart = i
            rowEnd = rowLength - 1 - i
            colStart = i
            colEnd = colLength - 1 - i
            if rowStart == rowEnd:
                ret.extend(matrix[rowStart][colStart : colEnd + 1])
                continue
            if colStart == colEnd:
                for row in range(rowStart, rowEnd + 1):
                    ret.append(matrix[row][colStart])
                continue
            for col in range(colStart, colEnd + 1):
                ret.append(matrix[rowStart][col])
            for row in range(rowStart + 1, rowEnd + 1):
                ret.append(matrix[row][colEnd])
            for col in range(colEnd - 1, colStart - 1, -1):
                ret.append(matrix[rowEnd][col])
            for row in range(rowEnd - 1, rowStart, -1):
                ret.append(matrix[row][colStart])
        return ret


# @lc code=end
