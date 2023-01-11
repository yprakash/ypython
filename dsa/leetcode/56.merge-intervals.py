# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/merge-intervals/submissions/876213279/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = deque()
        intervals.sort()

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                if stack[-1][1] < interval[1]:
                    it = stack.pop()
                    it[1] = interval[1]
                    stack.append(it)
            else:
                stack.append(interval)

        return list(stack)
