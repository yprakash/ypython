# @author: yprakash
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/917667577/
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] != 0 or grid[n][n] != 0:
            return -1

        grid[0][0] = 1  # modify/reuse grid instead of creating visited matrix
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        depth = 0
        q = deque()
        q.append((0, 0))

        while q:
            depth += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == n and j == n:
                    return depth

                for x, y in directions:
                    x, y = x + i, y + j
                    if 0 <= x <= n and 0 <= y <= n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))

        return -1
