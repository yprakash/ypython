# @author: yprakash
from collections import deque


class Solution(object):
    def __init__(self):
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, heights, reach, q):
        while q:
            row, col = q.popleft()
            if row < 0 or row >= len(reach) or col < 0 or col >= len(reach[0]) or reach[row][col]:
                continue  # Not within boundaries or already visited

            for r, c in self.directions:
                rr, cc = row+r, col+c
                if rr < 0 or rr >= len(reach) or cc < 0 or cc >= len(reach[0]):
                    continue
                # Now r, c are within the boundaries
                if reach[rr][cc] and heights[rr][cc] <= heights[row][col]:
                    reach[row][col] = True
                    break

            if reach[row][col]:
                for r, c in self.directions:
                    q.append((row+r, col+c))

    # https://leetcode.com/submissions/detail/788247161/
    def pacificAtlantic(self, heights):
        rangem, rangen = range(len(heights)), range(len(heights[0]))

        pacific = [[False] * len(heights[0]) for _ in rangem]
        pacific[0][0] = True
        p = deque()
        for i in range(1, len(heights)):
            pacific[i][0] = True
            p.append((i, 1))
        for i in range(1, len(heights[0])):
            pacific[0][i] = True
            p.append((1, i))

        self.bfs(heights, pacific, p)

        m, n = len(heights)-1, len(heights[0])-1
        atlantic = [[False] * len(heights[0]) for _ in rangem]
        atlantic[-1][-1] = True
        q = deque()
        for i in range(m):
            atlantic[i][n] = True
            q.append((i, n-1))
        for i in range(n):
            atlantic[m][i] = True
            q.append((m-1, i))

        self.bfs(heights, atlantic, q)

        result = []
        for r in rangem:
            for c in rangen:
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result

    def print_ocean(self, a):
        for i in range(len(a)):
            print(a[i])
        print('==============')


if __name__ == "__main__":
    testcases = [
        [[1]],  # [[0,0]]
        [[10, 10, 10],
         [10, 1, 10],
         [10, 10, 10]],  # [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]]  # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    ]
    obj = Solution()
    for mat in testcases:
        print(obj.pacificAtlantic(mat))
