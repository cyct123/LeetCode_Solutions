#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Medium (39.32%)
# Likes:    13295
# Dislikes: 1553
# Total Accepted:    1.4M
# Total Submissions: 3.6M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an integer array nums, rotate the array to the right by k steps, where
# k is non-negative.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
# Follow up:
#
#
# Try to come up with as many solutions as you can. There are at least three
# different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return
        lcm = self.lcm(len(nums), k)
        r = lcm // k
        for i in range(len(nums) // r):
            prev = nums[i]
            for _ in range(r):
                index = (i + k) % len(nums)
                cur = nums[index]
                nums[index] = prev
                prev = cur
                i = index

    def gcd(self, a: int, b: int) -> int:
        if not b:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a: int, b: int) -> int:
        if a > b:
            return a // self.gcd(a, b) * b
        return b // self.gcd(a, b) * a


# @lc code=end
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for i in range(len(nums)):
            res.append(nums[(i - k) % len(nums)])
        for i in range(len(nums)):
            nums[i] = res[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 4
    Solution().rotate(nums, k)
    print(nums)
