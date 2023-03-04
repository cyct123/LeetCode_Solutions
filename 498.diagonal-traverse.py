#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (58.23%)
# Likes:    2851
# Dislikes: 599
# Total Accepted:    238.5K
# Total Submissions: 409.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order.
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
#
# Example 2:
#
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j = 0, 0
        res = []
        for _ in range(len(mat) * len(mat[0])):
            res.append(mat[i][j])
            if not (i + j) % 2:
                if j == len(mat[0]) - 1:
                    i += 1
                elif not i:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == len(mat) - 1:
                    j += 1
                elif not j:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return res


# @lc code=end
