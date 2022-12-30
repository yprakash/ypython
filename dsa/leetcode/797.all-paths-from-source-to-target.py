# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/867804850/
class SolutionQ(object):
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph) - 1
        q = deque([[0]])

        while q:
            path = q.popleft()
            for node in graph[path[-1]]:
                if node == n:
                    res.append(path + [node])
                else:
                    q.append(path + [node])

        return res


class Solution(object):
    def recurse(self, graph, stack, res):
        if not stack:
            return
        peek = stack[-1]

        for edge in graph[peek]:
            stack.append(edge)
            if edge == len(graph) - 1:
                res.append(list(stack))
            else:
                self.recurse(graph, stack, res)
            stack.pop()

    # https://leetcode.com/submissions/detail/739468516/
    # Recursive Solution
    def allPathsSourceTarget(self, graph):
        res = []
        stack = deque([0])
        self.recurse(graph, stack, res)
        return res


obj = Solution()
print(obj.allPathsSourceTarget([[1], []]))  # [[0, 1]]
print(obj.allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0, 1, 3], [0, 2, 3]]
print(obj.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
# [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
