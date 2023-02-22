#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (33.45%)
# Likes:    3073
# Dislikes: 103
# Total Accepted:    322.4K
# Total Submissions: 958.4K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        step = 0
        visited = set([amount])
        queue = deque([amount])

        while queue:
            length = len(queue)
            step += 1
            for _ in range(length):
                cur = queue.popleft()
                for coin in coins:
                    if not cur - coin:
                        return step
                    if cur - coin > 0 and cur - coin not in visited:
                        visited.add(cur - coin)
                        queue.append(cur - coin)
        return -1


# @lc code=end
