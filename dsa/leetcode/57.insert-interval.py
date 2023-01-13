# @author: yprakash
from typing import List


# https://leetcode.com/problems/insert-interval/submissions/877344578/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        i, n = 0, len(intervals)

        while i < n and intervals[i][0] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1

        if not new_intervals:
            new_intervals.append(newInterval)
        elif new_intervals[-1][1] >= newInterval[1]:
            return intervals

        if new_intervals[-1][1] < newInterval[0]:
            new_intervals.append(newInterval)
        else:
            new_intervals[-1][1] = newInterval[1]

        while i < n and new_intervals[-1][1] >= intervals[i][0]:
            new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
            i += 1
        while i < n:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals


if __name__ == "__main__":
    testcases = [
        [[], [5, 7]],  # [[5, 7]]
        [[[1, 3], [6, 9]], [2, 5]],  # [[1, 5], [6, 9]]
        [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],  # [[1, 2], [3, 10], [12, 16]]
    ]
    for a, b in testcases:
        obj = Solution()
        print(obj.insert(a, b))
