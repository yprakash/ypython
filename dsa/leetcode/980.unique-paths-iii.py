# @author: yprakash
from typing import List


# https://leetcode.com/problems/unique-paths-iii/submissions/868398723/
class Solution:
    ans = 0

    def findPathNum(self, i, j, grid, cur_len, p_len):
        if grid[i][j] == 2:
            if p_len - 1 == cur_len:
                self.ans += 1
            return
        elif grid[i][j] == -1:
            return
        cur_len += 1
        grid[i][j] = -1
        if i - 1 >= 0:
            self.findPathNum(i - 1, j, grid, cur_len, p_len)
        if j - 1 >= 0:
            self.findPathNum(i, j - 1, grid, cur_len, p_len)
        if i + 1 < len(grid):
            self.findPathNum(i + 1, j, grid, cur_len, p_len)
        if j + 1 < len(grid[0]):
            self.findPathNum(i, j + 1, grid, cur_len, p_len)
        grid[i][j] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        path_len = 0
        start = (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    path_len += 1
                    if grid[i][j] == 1:
                        start = (i, j)
        self.findPathNum(start[0], start[1], grid, 0, path_len)
        return self.ans
