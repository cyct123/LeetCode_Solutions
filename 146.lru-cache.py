#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (40.57%)
# Likes:    16688
# Dislikes: 744
# Total Accepted:    1.3M
# Total Submissions: 3.1M
# Testcase Example:  '["LRUCache","put","put",
# "get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#
from collections import OrderedDict, deque


# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._map = OrderedDict()

    def get(self, key: int) -> int:
        if key in self._map:
            self._map.move_to_end(key)
        return self._map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self._map:
            if len(self._map) == self._capacity:
                last = next(iter(self._map))
                del self._map[last]
        else:
            del self._map[key]
        self._map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
class DequeLRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._queue = deque()
        self._map = {}

    def get(self, key: int) -> int:
        if key in self._map:
            self._queue.remove(key)
            self._queue.appendleft(key)
            return self._map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self._map:
            if len(self._queue) == self._capacity:
                last = self._queue.pop()
                del self._map[last]
        else:
            self._queue.remove(key)
        self._queue.appendleft(key)
        self._map[key] = value
