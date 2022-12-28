# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/756596236/
    def transpose(self, matrix):
        res = []
        rang = range(len(matrix))

        for c in range(len(matrix[0])):
            res.append([matrix[r][c] for r in rang])
        return res
