# @author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/submissions/876205178/
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        visited = [False] * n
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def time_to_collect(node):
            visited[node] = True
            if node in tree:  # non-leaf node
                total_time = sum(time_to_collect(child)
                                 for child in tree[node] if not visited[child])
                if total_time:
                    return 2 + total_time
            return 2 if hasApple[node] else 0

        ttc = time_to_collect(0)
        return ttc - 2 if ttc > 1 else 0
