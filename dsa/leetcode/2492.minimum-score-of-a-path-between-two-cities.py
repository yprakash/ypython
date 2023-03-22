# @author: yprakash
from collections import deque, defaultdict
from math import inf
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/submissions/920027455/
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        ans = 10000  # INT_MAX
        visited = set()
        visited.add(1)
        q = deque([1])

        while q:
            city = q.popleft()
            for c, d in adj[city]:
                ans = min(ans, d)
                if c not in visited:
                    q.append(c)
                    visited.add(c)

        return ans

    # https://leetcode.com/submissions/detail/854422816/
    # Only difference between 2 methods is type(visited)
    def minScore1(self, n: int, roads: List[List[int]]) -> int:
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
