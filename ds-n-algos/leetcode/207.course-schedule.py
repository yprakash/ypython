# @author: yprakash
from collections import deque, defaultdict


class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)

    # naive BFS INCORRECT
    def canFinish(self, numCourses, prerequisites):
        for prerequisite in prerequisites:
            self.graph[prerequisite[1]].append(prerequisite[0])

        # Courses can not be finished if Cycle exists
        def bfs(start, queue):
            visited = set()
            while queue:
                node = queue.popleft()
                visited.add(node)
                if node in self.graph:
                    for adj in self.graph[node]:
                        if adj == start:
                            return False
                        if adj not in visited:
                            queue.append(adj)
        # Inner method ENDs

        for node in self.graph:
            queue = deque()
            queue.append(node)
            if not bfs(node, queue):
                return False
        return True

    # https://leetcode.com/submissions/detail/761523243/
    # Using Topology sorting (Graphs) technique
    # TC: O(P+n*2) or O(P+n+E)
    # SC: O(n*2)
    def canFinish2(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            indegree[pair[0]] += 1
            adj_list[pair[1]].append(pair[0])

        stack = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                stack.append(i)

        visited_count = 0
        while stack:
            visited_count += 1
            for neighbour in adj_list[stack.popleft()]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    stack.append(neighbour)

        return visited_count == numCourses


testcases = [
    [2, [[1, 0]]],  # True
    [2, [[1, 0], [0, 1]]],  # False
    [6, [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]]  # True
]
for testcase in testcases:
    obj = Solution()
    print(obj.canFinish(testcase[0], testcase[1]))
