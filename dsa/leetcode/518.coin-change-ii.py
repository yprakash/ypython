# @author: yprakash
# https://leetcode.com/problems/coin-change-ii/submissions/1614349229/
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount + 1
        # Let dp[i] represent the number of ways to make amount i using the available coins.
        dp = [0] * n
        dp[0] = 1  # there is one way to make an amount of 0: use no coins.

        # For each coin in coins, we will update the DP table from coin to amount (inclusive). For every coin,
        # we check how we can contribute that coin to previously calculated amounts and accumulate the results.
        for coin in coins:
            for i in range(coin, n):
                dp[i] += dp[i - coin]
        return dp[amount]
