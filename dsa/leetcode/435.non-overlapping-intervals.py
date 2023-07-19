# @author: yprakash
from typing import List


# https://leetcode.com/problems/non-overlapping-intervals/submissions/998091638/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans, left, right = 0, 0, 1

        while right < len(intervals):
            if intervals[left][1] <= intervals[right][0]:
                # Non-overlapping case
                left = right
            else:
                ans += 1
            right += 1
        return ans


if __name__ == "__main__":
    testcases = [
        [[1, 2], [2, 3]],  # 0 NO need to remove any
        [[1, 2], [1, 2], [1, 2]],  # 2 remove two [1,2] to make others non-overlapping
        [[1, 2], [2, 3], [3, 4], [1, 3]],  # 1 remove [1, 3]
        [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99],
         [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]],  # 7
    ]
    for interval in testcases:
        obj = Solution()
        print(obj.eraseOverlapIntervals(interval))
