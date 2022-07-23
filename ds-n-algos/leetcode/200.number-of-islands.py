# @author: yprakash
from collections import deque


class Solution(object):
    def fill_island(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '0'

        self.fill_island(grid, row-1, col)
        self.fill_island(grid, row+1, col)
        self.fill_island(grid, row, col-1)
        self.fill_island(grid, row, col+1)

    # DFS: https://leetcode.com/submissions/detail/754419953/
    def numIslandsRec(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.fill_island(grid, i, j)

        return islands

    # BFS: https://leetcode.com/submissions/detail/754425289/
    def numIslands(self, grid):
        dqr = deque()  # DS to hold row indices
        dqc = deque()  # DS to hold column indices
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    dqr.append(i)
                    dqc.append(j)

                    while dqr:
                        row = dqr.popleft()
                        col = dqc.popleft()
                        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
                            continue
                        grid[row][col] = '0'

                        dqr.append(row-1)
                        dqc.append(col)
                        dqr.append(row+1)
                        dqc.append(col)
                        dqr.append(row)
                        dqc.append(col-1)
                        dqr.append(row)
                        dqc.append(col+1)

        return islands
