# @author: yprakash
from typing import List

from sortedcontainers import SortedList


# https://leetcode.com/problems/data-stream-as-disjoint-intervals/submissions/886968401/
class SummaryRanges:
    def __init__(self):
        self.sl = SortedList()

    def addNum(self, value: int) -> None:
        self.sl.add((value, value))

    def getIntervals(self) -> List[List[int]]:
        stack = []
        r = list(self.sl)
        self.sl = SortedList()

        for s, e in r:
            if stack and stack[-1][1] + 1 >= s:
                ps, pe = stack.pop()
                stack.append((min(ps, s), max(pe, e)))
            else:
                stack.append((s, e))

        for s, e in stack:
            self.sl.add((s, e))
        return stack


if __name__ == "__main__":
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)  # arr = [1]
    print(summaryRanges.getIntervals())  # return [[1, 1]]
    summaryRanges.addNum(3)  # arr = [1, 3]
    print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3]]
    summaryRanges.addNum(7)  # arr = [1, 3, 7]
    print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)  # arr = [1, 2, 3, 7]
    print(summaryRanges.getIntervals())  # return [[1, 3], [7, 7]]
    summaryRanges.addNum(6)  # arr = [1, 2, 3, 6, 7]
    print(summaryRanges.getIntervals())  # return [[1, 3], [6, 7]]
