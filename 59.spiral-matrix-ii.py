#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (67.12%)
# Likes:    4662
# Dislikes: 204
# Total Accepted:    425K
# Total Submissions: 632.2K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        startX, startY = 0, 0
        loop = n // 2
        mid = n // 2
        count = 1
        offset = 1
        while loop:
            i, j = startX, startY
            while i < n - offset:
                res[j][i] = count
                count += 1
                i += 1
            while j < n - offset:
                res[j][i] = count
                count += 1
                j += 1
            while i >= offset:
                res[j][i] = count
                count += 1
                i -= 1
            while j >= offset:
                res[j][i] = count
                count += 1
                j -= 1
            startX += 1
            startY += 1
            offset += 1
            loop -= 1
        if n % 2:
            res[mid][mid] = count
        return res


# @lc code=end
if __name__ == "__main__":
    n = 3
    print(Solution().generateMatrix(n))
