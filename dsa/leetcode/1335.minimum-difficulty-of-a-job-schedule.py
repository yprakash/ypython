# @author: yprakash
import math
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/823734994/
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[math.inf] * n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]  # Do first job on first day
        for i in range(1, n):
            # If there is only 1 day to finish first i jobs only
            dp[0][i] = max(jobDifficulty[i], dp[0][i-1])

        for i in range(1, d):
            for j in range(i, n):
                max_r = jobDifficulty[j]
                for r in range(j, i-1, -1):
                    max_r = max(max_r, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], max_r + dp[i-1][r-1])

        return dp[-1][-1]
