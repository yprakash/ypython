# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/756581686/
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if not matrix[r][c]:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
