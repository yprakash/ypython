# @author: yprakash
class Solution(object):
    def area_dfs(self, visited, grid, i, j):
        # It calculates max area starting from [i,j] position
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or not grid[i][j]:
            return 0

        visited[i][j] = True
        return 1 + self.area_dfs(visited, grid, i, j-1) + self.area_dfs(visited, grid, i-1, j) + \
               self.area_dfs(visited, grid, i, j+1) + self.area_dfs(visited, grid, i+1, j)

    # https://leetcode.com/submissions/detail/747790816/
    def maxAreaOfIsland(self, grid):
        visited = []
        for _ in range(len(grid)):
            visited.append([False] * len(grid[0]))

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.area_dfs(visited, grid, i, j)
                if max_area < area:
                    max_area = area

        return max_area


grids = [
    [[0, 0, 0, 0, 0, 0, 0, 0]],
    # ----------
    [[1, 1, 0, 1, 1],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [1, 1, 0, 1, 1]],
    # ----------
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
]
for g in grids:
    obj = Solution()
    print("MaxArea= ", str(obj.maxAreaOfIsland(g)))
