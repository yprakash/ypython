# @author: yprakash
import sys
from typing import List


class Solution:
    # https://leetcode.com/problems/cherry-pickup/submissions/920271938/
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dp(r1, c1, r2, c2):  # 4D dynamic programming using memoization
            if (r1, c1, r2, c2) in memoize:
                return memoize[(r1, c1, r2, c2)]
            if r1 > n or c1 > n or r2 > n or c2 > n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                # return something to indicate invalid path, 0 doesn't work
                return -sys.maxsize
            if r1 == c1 == n:  # and r2 == c2 == n not needed, as both would have taken same no.of steps
                return grid[r1][c1]

            if r1 == r2 and c1 == c2:
                curr_cherry = grid[r1][c1]
            else:
                curr_cherry = grid[r1][c1] + grid[r2][c2]

            next_cherries = -sys.maxsize
            for r1d, c1d in directions:
                for r2d, c2d in directions:
                    nr1 = r1 + r1d
                    nc1 = c1 + c1d
                    nr2 = r2 + r2d
                    nc2 = c2 + c2d
                    next_cherries = max(next_cherries, dp(nr1, nc1, nr2, nc2))

            # If all 4 paths from current position are invalid, then current path should also be invalid
            # which is possible only when we returned negative infinity in base case
            curr_cherry += next_cherries
            memoize[(r1, c1, r2, c2)] = curr_cherry
            return curr_cherry

        directions = [(0, 1), (1, 0)]  # right or down
        n = len(grid) - 1
        memoize = {}
        ans = dp(0, 0, 0, 0)
        return ans if ans > 0 else 0

    # https://leetcode.com/problems/cherry-pickup/submissions/920149039/
    # Wrong Answer for testcase 3
    def cherryPickup3(self, grid: List[List[int]]) -> int:
        reached, n = False, len(grid) - 1

        def backtrack(r, c):
            if r == n and c == n:
                nonlocal reached
                reached = True
            if r > n or c > n or grid[r][c] == -1:
                return 0

            right = backtrack(r, c + 1)
            down = backtrack(r + 1, c)
            if grid[r][c] == 0:
                return right + down

            grid[r][c] = 0
            return 1 + right + down

        cherries = backtrack(0, 0)
        if not reached:
            return 0
        return cherries + backtrack(0, 0)


if __name__ == "__main__":
    testcases = [
        [[0, 1, -1], [1, 0, -1], [1, 1, 1]],  # 5
        [[1, 1, -1], [1, -1, 1], [-1, 1, 1]],  # 0 can't reach to end
        [[0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [-1, 1, 1, 1, -1], [0, 1, 1, 1, 0], [1, 0, -1, 0, 0]],  # 11
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.cherryPickup(testcase))
