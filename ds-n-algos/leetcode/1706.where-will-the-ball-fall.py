# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/834425987/
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = [-1] * n

        for i in range(n):
            r, c = 0, i
            while r < m:
                if grid[r][c] == 1:  # top-left to the bottom-right corner
                    if c < n-1 and grid[r][c+1] == 1:
                        r += 1
                        c += 1
                    else:
                        break

                elif grid[r][c] == -1:  # top-right to the bottom-left corner
                    if c > 0 and grid[r][c-1] == -1:
                        r += 1
                        c -= 1
                    else:
                        break

            if r == m:
                answer[i] = c

        return answer
