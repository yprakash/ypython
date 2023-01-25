# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/problems/find-closest-node-to-given-two-nodes/submissions/884775497/
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        path1, path2 = set(), set()

        # RecursionError: maximum recursion depth exceeded while calling a Python object
        #     path1.add(u)
        def dfs(u, v):
            path1.add(u)
            path2.add(v)
            if v in path1:
                if u in path2:
                    return min(u, v)  # If there are multiple answers
                return v
            if u in path2:
                return u
            if edges[u] == -1 and edges[v] == -1:
                return -1

            if edges[u] == -1:
                return dfs(u, edges[v])
            if edges[v] == -1:
                return dfs(edges[u], v)
            return dfs(edges[u], edges[v])

        return dfs(node1, node2)
