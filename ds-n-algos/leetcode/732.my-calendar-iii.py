# @author: yprakash
from sortedcontainers import SortedList


# https://leetcode.com/submissions/detail/834106963/
class MyCalendarThree:
    def __init__(self):
        self.times = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        self.times.add((startTime, True))
        self.times.add((endTime, False))
        ans, concurrent = 0, 0

        for _, e in self.times:
            if e:
                concurrent += 1
                if ans < concurrent:
                    ans = concurrent
            else:
                concurrent -= 1

        return ans
