# @author: yprakash
from typing import List


class OrderedStream:
    # https://leetcode.com/submissions/detail/825879957/
    def __init__(self, n: int):
        self.stream = [None] * (n + 2)
        self.ptr = 1  # Starting pointer

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if self.ptr != idKey:
            return []

        res = []
        while self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res
