# @author: yprakash
from collections import deque


class Solution(object):
    # We can't use DFS for this kind of problems. BFS is the only way
    # BFS: https://leetcode.com/submissions/detail/754440427/
    def orangesRotting(self, grid):
        dq_rotten = deque()  # DS to hold already rotten oranges

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:  # rotten orange
                    dq_rotten.append(i)
                    dq_rotten.append(j)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minutes = 0
        while dq_rotten:
            dq_fresh = deque()  # DS to hold fresh orange Indices

            while dq_rotten:
                row = dq_rotten.popleft()
                col = dq_rotten.popleft()

                for dir in directions:
                    r = row+dir[0]
                    c = col+dir[1]
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                        continue

                    dq_fresh.append(r)
                    dq_fresh.append(c)
                    grid[r][c] = 2

            if dq_fresh:
                minutes += 1
                dq_rotten = dq_fresh

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Fresh orange remains
                    return -1
        return minutes
