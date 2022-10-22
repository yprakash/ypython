# @author: yprakash
from collections import deque


class FrontMiddleBackQueue:
    # https://leetcode.com/submissions/detail/827613542/
    def __init__(self):
        # For an O(1), use 2 double-ended queues: one for the first half and one for the second half.
        # Always ensure len(first) is equal to or just one more than len(second)
        self.first = deque()
        self.second = deque()

    def pushFront(self, val: int) -> None:
        if len(self.first) == len(self.second):
            self.first.appendleft(val)
            # middle element = first[-1] won't change
        else:
            self.second.appendleft(self.first.pop())
            self.first.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        if len(self.first) == len(self.second):
            self.first.append(val)
        else:
            self.second.appendleft(self.first.pop())
            self.first.append(val)

    def pushBack(self, val: int) -> None:
        if not self.first:
            self.first.append(val)
            return  # Mandatory to avoid next append

        if len(self.first) == len(self.second):
            self.first.append(self.second.popleft())
        self.second.append(val)

    def popFront(self) -> int:
        if not self.first:
            return -1
        if len(self.first) == len(self.second):
            self.first.append(self.second.popleft())
        return self.first.popleft()

    def popMiddle(self) -> int:
        if not self.first:
            return -1
        if len(self.first) == len(self.second):
            val = self.first.pop()
            self.first.append(self.second.popleft())
            return val
        return self.first.pop()

    def popBack(self) -> int:
        if not self.first:
            return -1
        if len(self.first) == len(self.second):
            return self.second.pop()
        self.second.appendleft(self.first.pop())
        return self.second.pop()
