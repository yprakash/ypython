# @author: yprakash
from collections import deque, defaultdict
from math import inf
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/854422816/
    # Only difference between 2 methods is type(visited)
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for s, t, d in roads:
            adj_list[s].append((t, d))
            adj_list[t].append((s, d))

        score = 10000
        visited = [False] * (n+1)
        q = deque()
        q.append(1)

        while q:
            s = q.popleft()
            visited[s] = True
            for t, d in adj_list[s]:
                score = min(score, d)
                if not visited[t]:
                    q.append(t)

        return score

    # TLE  https://leetcode.com/submissions/detail/854420415/
    def minScore2(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for s, t, d in roads:
            adj_list[s].append((t, d))
            adj_list[t].append((s, d))

        score = inf
        visited = set()
        q = deque()
        q.append(1)

        while q:
            s = q.popleft()
            visited.add(s)
            for t, d in adj_list[s]:
                score = min(score, d)
                if t not in visited:
                    q.append(t)

        return score
