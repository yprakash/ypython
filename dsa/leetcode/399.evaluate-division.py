# @author: yprakash
from collections import defaultdict, deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/852599978/
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # n: no.of currencies amd m: no.of edges/pairs
        adj_list = defaultdict(list)  # O(m)
        for i, value in enumerate(values):
            s, t = equations[i]
            adj_list[s].append((t, value))
            adj_list[t].append((s, 1 / value))

        def calc_query(src, target):
            q = deque()
            q.append((src, 1))
            visited = set()

            while q:  # O(m)
                node, rate_prev = q.popleft()
                visited.add(node)
                for adj, rate in adj_list[node]:
                    result_rate = rate * rate_prev
                    if adj == target:
                        return result_rate
                    if adj not in visited:
                        q.append((adj, result_rate))
            return -1

        return [calc_query(s, t) for s, t in queries]
