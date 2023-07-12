# @author: yprakash
from typing import List


# https://leetcode.com/problems/find-eventual-safe-states/submissions/992870307/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if terminal[node] == 1:
                return True
            if terminal[node] == -1 or visited[node]:
                return False

            visited[node] = True
            for edge in graph[node]:
                if not dfs(edge):
                    terminal[node] = -1
                    break
            if terminal[node] == 0:
                terminal[node] = 1
            return terminal[node] == 1

        visited = [False] * len(graph)
        terminal = [0] * len(graph)
        for i in range(len(graph)):
            dfs(i)
        return [i for i in range(len(graph)) if terminal[i] == 1]
