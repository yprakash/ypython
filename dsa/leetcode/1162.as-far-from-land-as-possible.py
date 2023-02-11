# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/as-far-from-land-as-possible/submissions/896112076/
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        distance = -1
        n = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def can_move(x, y):
            return 0 <= x < n and 0 <= y < n and not grid[x][y]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = True
                    q.append((i, j))
                else:
                    grid[i][j] = False

        if len(q) == 0 or len(q) == n * n:
            return -1

        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                for x, y in directions:
                    if can_move(x + i, y + j):
                        grid[x + i][y + j] = True
                        q.append((x + i, y + j))

            distance += 1
        return distance
