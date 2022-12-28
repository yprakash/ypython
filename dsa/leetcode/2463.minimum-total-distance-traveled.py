# @author: yprakash
from math import inf
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/838090676/
    # Partially correct O(R*F).
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        R = len(robot)
        factory.sort()
        F = len(factory)

        # Find the minimum total distance to repair first i robots with first j factories.
        dp = [[inf] * F for _ in range(R)]
        # If there is only 1 robot and 1 factory
        dp[0][0] = abs(factory[0][0] - robot[0])

        limit = [0] * F
        cum_limit = factory[0][1]
        limit[0] = cum_limit

        # If there is 1 robot and f factories
        for j in range(1, F):
            cum_limit += factory[j][1]
            limit[j] = cum_limit
            dp[0][j] = min(dp[0][j-1], abs(factory[j][0] - robot[0]))
        # print(dp[0])

        # If there are r robots and 1 factory, only factory[0][1] robots can travel
        for i in range(1, min(R, factory[0][1])):
            dp[i][0] = dp[i-1][0] + abs(factory[0][0] - robot[i])

        for i in range(1, R):
            dist = inf
            for j in range(1, F):
                # dist = min(dist, abs(factory[j][0] - robot[i]))
                dist = abs(factory[j][0] - robot[i])

                if limit[j] - i > 1:  # both i-1 and i robots can be repaired at j factory
                    dp[i][j] = min(dist + dp[i-1][j-1], dp[i][j-1])
                elif limit[j] - i > 0:  # only i can be repaired at j, hence till i-1 must be within j-1
                    dp[i][j] = dist + dp[i-1][j-1]

            # print(dp[i], dist)
        return int(dp[-1][-1])


if __name__ == "__main__":
    testcases = [
        [[0, 4], [[2, 2]]],  # 4
        [[0, 4, 6], [[2, 2], [6, 2]]],  # 4
        [[1, -1], [[-2, 1], [2, 1]]],  # 2
        [[9, 11], [[10, 1], [7, 1], [14, 1]]],  # 3
        [[9, 11, 99, 101], [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]]],  # 6

        # Failed for this
        [[670355988, 403625544, 886437985, 224430896, 126139936, -477101480, -868159607, -293937930],
         [[333473422, 7], [912209329, 7], [468372740, 7], [-765827269, 4],
          [155827122, 4], [635462096, 2], [-300275936, 2], [-115627659, 0]]],  # 509199280
    ]
    for r, f in testcases:
        obj = Solution()
        print(obj.minimumTotalDistance(r, f))
