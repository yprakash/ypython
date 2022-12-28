# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/838681067/
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += 2 + 4 * grid[i][j]
                if i:
                    area -= 2 * min(grid[i][j], grid[i-1][j])
                if j:
                    area -= 2 * min(grid[i][j], grid[i][j-1])

        return area
