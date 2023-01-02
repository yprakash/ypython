# @author: yprakash
from bisect import bisect_left
from sys import maxsize
from typing import List


# WA https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/submissions/868335205/
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def max_subarray_sum(some, k, row):
            curr_sum, curr_max = 0, -maxsize - 1
            sum_set = {0: 1}

            for r in range(row):
                curr_sum += some[r]
                arr = list(sum_set.keys())
                it = bisect_left(arr, curr_sum - k)
                if it != len(arr):
                    curr_max = max(curr_max, curr_sum - it)
                sum_set[curr_sum] = 1
            return curr_max

        row = len(matrix)
        col = len(matrix[0])
        res = -maxsize - 1
        for i in range(col):
            some = [0] * row

            for j in range(i, col):
                for r in range(row):
                    some[r] += matrix[r][j]
                cur_max = max_subarray_sum(some, k, row)
                res = max(res, cur_max)

        return res
