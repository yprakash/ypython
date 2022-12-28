# @author: yprakash
from collections import deque, defaultdict
from numpy import zeros, where


class Solution(object):
    # https://leetcode.com/submissions/detail/739064404/
    def validPath(self, n, edges, source, destination):
        paths = defaultdict(set)
        for edge in edges:
            paths[edge[0]].add(edge[1])
            paths[edge[1]].add(edge[0])

        visited = set()
        stack = deque()
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            visited.add(node)
            [stack.append(x) for x in paths[node] if x not in visited]

        return False

    # MemoryError while initializing numpy 2D array of bools when n=100000
    # https://leetcode.com/submissions/detail/739040896/
    def validPath3(self, n, edges, source, destination):
        nodes = zeros((n, n), dtype=bool)
        for edge in edges:
            nodes[edge[0]][edge[1]] = True
            nodes[edge[1]][edge[0]] = True

        visited = set()
        stack = deque()
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)

            for x in where(nodes[node]):
                [stack.append(y) for y in x if y not in visited]

        return False


obj = Solution()
print(obj.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  #
print(obj.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  #
