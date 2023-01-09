# @author: yprakash
from collections import defaultdict
from math import gcd
from typing import List


# https://leetcode.com/problems/max-points-on-a-line/submissions/874373809/
# https://www.geeksforgeeks.org/count-maximum-points-on-same-line/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def normalized_slope(a, b):
            run = b[0] - a[0]
            if run == 0:
                return (1, 0)
            if run < 0:
                a, b = b, a
                run = b[0] - a[0]
            rise = b[1] - a[1]
            gcd_ = gcd(abs(rise), run)
            return (rise // gcd_, run // gcd_)

        if len(points) < 3:
            return len(points)
        max_val = 0

        for i in range(len(points) - 1):
            a = tuple(points[i])
            slope_counts = defaultdict(lambda: 1)
            for j in range(i+1, len(points)):
                b = tuple(points[j])
                slope_counts[normalized_slope(a, b)] += 1

            max_val = max(max_val, max(slope_counts.values()))
        return max_val
