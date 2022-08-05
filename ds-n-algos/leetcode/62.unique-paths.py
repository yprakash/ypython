# author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/762028754/
    def uniquePaths(self, m, n):
        paths = [[1 for _ in range(n)] for j in range(m)]
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                paths[r][c] = paths[r+1][c] + paths[r][c+1]
        return paths[0][0]
