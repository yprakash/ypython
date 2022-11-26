# @author: yprakash
import bisect

from sortedcontainers import SortedList


class TimeMap:
    # https://leetcode.com/submissions/detail/849608802/
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = SortedList()
        self.map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''

        index = bisect.bisect_right(self.map[key], timestamp, key=lambda tv: tv[0])
        return self.map[key][index - 1][1] if index > 0 else ''
