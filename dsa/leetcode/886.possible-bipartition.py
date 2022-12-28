# @author: yprakash
from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/possible-bipartition/submissions/863386502/
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for s, t in dislikes:
            graph[s].append(t)
            graph[t].append(s)

        color = [0] * (n + 1)
        for vertex in graph:
            if color[vertex] != 0:
                continue
            q = deque()
            q.append(vertex)
            color[vertex] = 1

            while q:
                vertex = q.popleft()
                clr = color[vertex]
                for t in graph[vertex]:
                    if color[t] == clr:
                        return False
                    if color[t] == 0:  # t is not yet visited
                        color[t] = -1 if clr == 1 else 1
                        q.append(t)

        return True
