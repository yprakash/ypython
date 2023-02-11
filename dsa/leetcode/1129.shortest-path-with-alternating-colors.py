# @author: yprakash
import math
from collections import deque, defaultdict
from typing import List


# https://leetcode.com/problems/shortest-path-with-alternating-colors/submissions/896079884/
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [math.inf] * n
        adj = defaultdict(list)
        for u, v in redEdges:
            adj[u].append((v, False))
        for u, v in blueEdges:
            adj[u].append((v, True))

        def traverse(color):
            q = deque()
            q.append((color, 0, 0))
            visited = set()
            while q:
                color, node, dist = q.popleft()
                visited.add((node, color))
                if dist < answer[node]:
                    answer[node] = dist

                for v, c in adj[node]:
                    if c != color and (v, c) not in visited:
                        q.append((c, v, dist + 1))

        traverse(True)
        traverse(False)
        for i, a in enumerate(answer):
            if a == math.inf:
                answer[i] = -1
        return answer
