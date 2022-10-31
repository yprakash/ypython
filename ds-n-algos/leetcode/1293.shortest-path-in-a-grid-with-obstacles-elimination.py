# @author: yprakash
import math
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/834036664/
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        obstacles = [[math.inf] * n for _ in range(m)]  # Fill it with min no.of obstacles needed to remove to reach grid[i,j]
        obstacles[0][0] = grid[0][0]
        q = deque()
        q.append([0, 0, grid[0][0]])
        level = 0

        while q:
            curr_size = len(q)
            while curr_size > 0:
                cell = q.popleft()
                curr_size -= 1
                if cell[0] == m - 1 and cell[1] == n - 1:
                    return level
                curr_obstacle_count = cell[2]

                for x, y in directions:
                    x += cell[0]
                    y += cell[1]
                    if not (0 <= x < m and 0 <= y < n):
                        continue

                    old_obstacle_count = obstacles[x][y]
                    new_obstacle_count = curr_obstacle_count + grid[x][y]

                    if old_obstacle_count > new_obstacle_count and new_obstacle_count <= k:
                        q.append([x, y, new_obstacle_count])
                        obstacles[x][y] = new_obstacle_count

            level += 1

        return -1


if __name__ == "__main__":
    testcases = [
        [1, [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]],  # 6
        [1, [[0, 1, 1], [1, 1, 1], [1, 0, 0]]],  # -1
    ]
    for kk, gg in testcases:
        obj = Solution()
        print(obj.shortestPath(gg, kk))
