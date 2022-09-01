# @author: yprakash

class Solution(object):
    def sort_diag(self, mat, m, n):
        tmp = []
        i, j = m, n

        while i < len(mat) and j < len(mat[0]):
            tmp.append(mat[i][j])
            i += 1
            j += 1

        tmp.sort()
        i, j, k = m, n, 0
        while i < len(mat) and j < len(mat[0]):
            mat[i][j] = tmp[k]
            i += 1
            j += 1
            k += 1

    # https://leetcode.com/submissions/detail/785167881/
    def diagonalSort(self, mat):
        for i in range(len(mat)):
            self.sort_diag(mat, i, 0)
        for j in range(1, len(mat[0])):
            self.sort_diag(mat, 0, j)
        return mat
