# @author: yprakash
from typing import List


# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/submissions/885828035/
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        a, b = node1, node2
        path1, path2 = set(), set()

        while a != -1 and b != -1:
            if a in path1 or b in path2:
                break
            path1.add(a)
            path2.add(b)
            if b in path1:
                if a in path2:
                    return min(a, b)  # If there are multiple answers
                return b
            if a in path2:
                return a
            a = edges[a]
            b = edges[b]

        while a != -1 and a not in path1:
            path1.add(a)
            if a in path2:
                return a
            a = edges[a]

        while b != -1 and b not in path2:
            path2.add(b)
            if b in path1:
                return b
            b = edges[b]

        return -1

    # https://leetcode.com/problems/find-closest-node-to-given-two-nodes/submissions/884775497/
    def closestMeetingNode2(self, edges: List[int], node1: int, node2: int) -> int:
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


if __name__ == "__main__":
    testcases = [
        [[1, 2, -1], 0, 2]
    ]
    for e, n1, n2 in testcases:
        obj = Solution()
        print(obj.closestMeetingNode2(e, n1, n2))
