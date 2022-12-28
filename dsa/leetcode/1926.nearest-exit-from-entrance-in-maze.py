# @author: yprakash
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/847194536/
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def add_neighbours(i, j):
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]
                if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                    maze[x][y] = '+'  # This is to avoid adding same point multiple times
                    q.append((x, y))

        distance = 1
        maze[entrance[0]][entrance[1]] = '+'
        add_neighbours(entrance[0], entrance[1])

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    return distance
                add_neighbours(x, y)

            distance += 1

        return -1
