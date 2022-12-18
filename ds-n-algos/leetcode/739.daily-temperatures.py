# @author: yprakash
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/problems/daily-temperatures/submissions/861380338/
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        stack.append((temperatures[-1], len(temperatures)-1))
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))

        return answer
