# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/834115893/
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(n-1):
            elem = matrix[0][i]
            r, c = 1, i + 1
            while r < m and c < n:
                if matrix[r][c] != elem:
                    return False
                r += 1
                c += 1

        for i in range(1, m-1):
            elem = matrix[i][0]
            r, c = i + 1, 1
            while r < m and c < n:
                if matrix[r][c] != elem:
                    return False
                r += 1
                c += 1

        return True
