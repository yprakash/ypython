# @author: yprakash
from functools import cache
from typing import List


class Solution(object):
    # https://leetcode.com/submissions/detail/849857190/
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()

        @cache  # memoize
        def profit(i):
            if i >= n:
                return 0
            # Do binary search for the immediate next index that can run after current job
            lo, hi = i + 1, n - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if jobs[mid][0] < jobs[i][1]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return max(profit(i + 1),  # Don't run curr job
                       profit(lo) + jobs[i][2])

        return profit(0)
