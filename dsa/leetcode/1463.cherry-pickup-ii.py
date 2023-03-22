# @author: yprakash
from typing import List


# https://leetcode.com/problems/cherry-pickup-ii/submissions/920290228/
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dp(r, c1, c2):  # 3D Dynamic programming
            if r >= len(grid) or not 0 <= c1 < c2 <= n:
                return 0
            if (r, c1, c2) in memoize:
                return memoize[(r, c1, c2)]

            next_cherries = 0
            for nc1 in directions:
                for nc2 in directions:
                    next_cherries = max(next_cherries, dp(r + 1, c1 + nc1, c2 + nc2))

            curr_cherry = grid[r][c1] + grid[r][c2] + next_cherries
            memoize[(r, c1, c2)] = curr_cherry
            return curr_cherry

        directions = [-1, 0, 1]
        memoize = {}
        n = len(grid[0]) - 1  # no.of cols - 1
        return dp(0, 0, n)
