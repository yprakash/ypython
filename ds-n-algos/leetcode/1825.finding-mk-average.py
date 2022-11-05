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


def _cleanup(heap):
    while heap and heap[0].deleted:
        heapq.heappop(heap)


class MKAverage:  # InComplete addElement method
    class Node:
        def __init__(self, val):
            self.val = val
            self.deleted = False
            self.next = None

        # Write a wrapper class that overrides ‘<‘ operator, as heapq only accepts iterables
        def __lt__(self, other):
            return self.val < other.val

    def __init__(self, m: int, k: int):
        self.k = k
        self.m = m
        self.sum = 0
        self.head = None
        self.tail = None
        self.max_heap1 = []  # to store first part
        self.min_heap2 = []  # to store middle part
        self.min_heap3 = []  # to store last part
        self.n = 0  # exact length of all 3 lists above (excluding deleted)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        return self.sum // self.n  # O(1)

    def addElement(self, num: int) -> None:
        if not self.head:
            self.head = self.tail = self.Node(num)
            self.max_heap1.append(self.head)
            return

        if self.n == self.m:
            _cleanup(self.min_heap2)  # continue
            if self.head.val < self.min_heap2[0].val:
                # item to be removed is in self.max_heap1 first part
                self.sum -= self.min_heap2[0].val
                self.sum += self.min_heap3[0].val
                heapq.heappush(self.max_heap1, heapq.heappop(self.min_heap2))
            # we need remove head element
            self.head.deleted = True
            self.head = self.head.next

        if len(self.max_heap1) < self.k:
            self.tail.next = self.Node(num)
            self.tail = self.tail.next
            heapq.heappush(self.max_heap1, self.tail)
