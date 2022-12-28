# @author: yprakash
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.stream = deque(maxlen=size)

    def next(self, val: int) -> float:
        if len(self.stream) == self.size:
            self.sum -= self.stream.popleft()

        self.stream.append(val)
        self.sum += val
        return self.sum / len(self.stream)
