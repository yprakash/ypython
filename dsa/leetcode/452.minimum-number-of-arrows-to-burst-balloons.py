# @author: yprakash
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        i, y, arrows = 0, 0, 0
        points.sort(key=lambda x: x[1])

        while True:
            if i < len(points):
                y = points[i][1]
                arrows += 1
            else:
                break
            while i < len(points) and points[i][0] <= y:
                i += 1

        return arrows
