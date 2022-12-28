# @author: yprakash

# https://leetcode.com/problems/domino-and-tromino-tiling/submissions/864522794/
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n

        mod = 1e9 + 7
        dp = [[0] * 3 for i in range(n+1)]
        dp[0][0] = 1
        dp[1][0] = dp[1][1] = dp[1][2] = 1

        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] +
                        dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod

        return int(dp[n][0])
