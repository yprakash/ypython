# @author: yprakash
import heapq
from collections import deque
from sortedcontainers import SortedList


class MKAverage1:  # Correct but Time Limit Exceeded bcoz of O(m) calculateMKAverage
    # https://leetcode.com/submissions/detail/836696970/
    def __init__(self, m: int, k: int):
        self.k = k
        self.m = m
        self.n = m - 2 * k
        self.list = SortedList()
        self.q = deque(maxlen=m)

    def addElement(self, num: int) -> None:
        if len(self.q) == self.m:
            value = self.q.popleft()  # O(1)
            self.list.remove(value)  # O(log N)

        self.list.add(num)
        self.q.append(num)  # O(log N)

    def calculateMKAverage(self) -> int:
        if len(self.q) == self.m:
            return sum(self.list.islice(self.k, self.m - self.k)) // self.n  # O(m)
        return -1


# Accepted using O(1) calculateMKAverage and O(6 * log m) add
# https://leetcode.com/submissions/detail/836726892/
class MKAverage2:
    def __init__(self, m: int, k: int):
        self.k = k
        self.m = m
        self.sum = 0
        self.n = m - 2 * k
        self.list = SortedList()
        self.q = deque(maxlen=m)

    def addElement(self, num: int) -> None:
        if len(self.q) == self.m:
            value = self.q.popleft()  # O(1)

            index = self.list.index(value)  # we can also use bisect_left
            if index < self.k:  # Element to be removed is in the first part
                self.sum -= self.list.__getitem__(self.k)
                self.sum += self.list.__getitem__(self.m - self.k)
            elif index < self.m - self.k:  # Element to be removed is in the middle
                self.sum -= value
                self.sum += self.list.__getitem__(self.m - self.k)
            # else:  # No need to modify the sum if Element to be removed is in the last part

            self.list.remove(value)  # O(log N)

        index = self.list.bisect_right(num)
        self.list.add(num)  # should come only after getting above index
        self.q.append(num)

        if index < self.k:  # Element to be added is in the first part
            if len(self.q) > self.k:
                self.sum += self.list.__getitem__(self.k)
                if len(self.q) > self.m - self.k:
                    self.sum -= self.list.__getitem__(self.m - self.k)

        elif index < self.m - self.k:  # Element to be added is in the middle
            self.sum += num
            if len(self.q) > self.m - self.k:
                self.sum -= self.list.__getitem__(self.m - self.k)
        # else:  # No need to modify the sum if Element to be added is in the last part

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        return self.sum // self.n  # O(1)
