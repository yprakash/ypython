# @author: yprakash
from collections import defaultdict, deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/843430759/
    def removeStones(self, stones: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x1, y1 in stones:
            for x2, y2 in stones:
                if x1 == x2 or y1 == y2:
                    adj[(x1, y1)].append((x2, y2))

        visited = set()
        disjoints = 0
        q = deque()
        for vertex in adj.keys():
            if vertex in visited:
                continue
            disjoints += 1
            q.append(vertex)
            visited.add(vertex)

            while q:
                vertex = q.popleft()
                for edge in adj[vertex]:
                    if edge not in visited:
                        q.append(edge)
                        visited.add(edge)

        return len(stones) - disjoints
