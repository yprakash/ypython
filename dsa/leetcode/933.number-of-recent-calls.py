# @author: yprakash
from collections import deque


class RecentCounter:
    # https://leetcode.com/submissions/detail/825871032/
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
