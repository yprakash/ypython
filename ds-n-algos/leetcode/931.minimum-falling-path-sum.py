# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-falling-path-sum/submissions/859220053/
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n <= 1:
            return matrix[0][0]

        for i in range(n - 2, -1, -1):
            matrix[i][0] += min(matrix[i+1][0], matrix[i+1][1])
            matrix[i][-1] += min(matrix[i+1][-1], matrix[i+1][-2])
            for j in range(1, n - 1):
                matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1])

        return min(matrix[0])
