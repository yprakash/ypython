# @author: yprakash
import heapq
from typing import List


# https://leetcode.com/problems/single-threaded-cpu/submissions/867230433/
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort()
        n = len(tasks)
        heap, answer = [], []

        i, t = 0, 0
        while True:
            if not heap and i < n and t < tasks[i][0]:
                t = tasks[i][0]
            while i < n and tasks[i][0] <= t:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not heap:
                break
            a, b = heapq.heappop(heap)
            t += a
            answer.append(b)
        return answer
