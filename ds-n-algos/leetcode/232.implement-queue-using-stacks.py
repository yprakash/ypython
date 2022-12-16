# @author: yprakash
from collections import deque


# https://leetcode.com/submissions/detail/731123646/
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def fill_up(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.fill_up()
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        self.fill_up()
        return self.stack2[-1] if self.stack2 else None  # peek()= lst[-1] O(1)

    def empty(self):
        self.fill_up()
        # return len(self.stack2) == 0
        return False if self.stack2 else True


# https://leetcode.com/problems/implement-queue-using-stacks/submissions/860437996/
class MyQueue2:  # python3
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


obj = MyQueue()
obj.push('prakash')
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
