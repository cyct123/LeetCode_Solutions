#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (55.88%)
# Likes:    3212
# Dislikes: 890
# Total Accepted:    366.9K
# Total Submissions: 649.5K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).
#
# Implement the MyStack class:
#
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
#
#
#
# Follow-up: Can you implement the stack using only one queue?
#
#
from collections import deque


# @lc code=start
class MyStack:
    def __init__(self):
        self._queue1 = deque()
        self._queue2 = deque()
        self._length = 0

    def push(self, x: int) -> None:
        self._queue1.append(x)
        self._length += 1

    def pop(self) -> int:
        for _ in range(self._length - 1):
            self._queue2.append(self._queue1.popleft())
        self._length -= 1
        self._queue1, self._queue2 = self._queue2, self._queue1
        return self._queue2.popleft()

    def top(self) -> int:
        for _ in range(self._length - 1):
            self._queue2.append(self._queue1.popleft())
        num = self._queue1.popleft()
        self._queue2.append(num)
        self._queue1, self._queue2 = self._queue2, self._queue1
        return num

    def empty(self) -> bool:
        return not self._queue1 and not self._queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
