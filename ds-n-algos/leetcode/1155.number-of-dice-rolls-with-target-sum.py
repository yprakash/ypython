# @author: yprakash
from functools import lru_cache


class Solution:
    # https://leetcode.com/submissions/detail/813264674/
    @lru_cache(maxsize=None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            return int(0 < target <= k)

        res = 0
        for i in range(1, k+1):
            res += self.numRollsToTarget(n-1, k, target-i)
        return res % (7 + 10 ** 9)

    # https://leetcode.com/submissions/detail/813261529/
    # Bottom up DP solution
    def numRollsToTargetDP(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0
        mod = 7 + 10 ** 9
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, target+1):
                for x in range(1, k+1):
                    if j-x >= 0:
                        dp[i][j] = (dp[i][j] % mod + dp[i - 1][j - x] % mod) % mod

        return dp[n][target]


if __name__ == "__main__":
    testcases = [
        [1, 6, 3],  # 1
        [2, 6, 7],  # 6
        [30, 30, 500],  # 222616187
    ]
    for n, k, t in testcases:
        obj = Solution()
        print(obj.numRollsToTarget(n, k, t))
