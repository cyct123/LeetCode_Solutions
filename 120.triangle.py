#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (42.15%)
# Likes:    1591
# Dislikes: 189
# Total Accepted:    223K
# Total Submissions: 526.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pathSum = []
        for i in range(len(triangle)):
            if i == 0:
                lineSum = [triangle[0][0]]
            else:
                lineSum = [num for num in triangle[i]]
                for j in range(i+1):
                    if j == 0:
                        lineSum[j] += pathSum[i-1][j]
                    elif j == i:
                        lineSum[j] += pathSum[i-1][j-1]
                    else:
                        smaller = min(pathSum[i-1][j], pathSum[i-1][j-1])
                        lineSum[j] += smaller
            pathSum.append(lineSum)
        return min(pathSum[-1])


# @lc code=end

