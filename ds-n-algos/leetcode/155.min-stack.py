# @author: yprakash
from collections import deque


# https://leetcode.com/submissions/detail/813308906/
class MinStack(object):
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        mn = val
        if self.stack:
            _, mn = self.stack[-1]
            if mn > val:
                mn = val
        self.stack.append((val, mn))

    def pop(self):
        top, _ = self.stack.pop()
        return top

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()