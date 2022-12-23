# @author: yprakash
from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/864007176/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        ndays = len(prices)

        buy = [0] * ndays
        sell = [0] * ndays

        buy[0] = -prices[0]
        buy[1] = max(-prices[1], buy[0])

        sell[0] = 0
        sell[1] = max(buy[0] + prices[1], sell[0])

        for i in range(2, ndays):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])

        return max(buy[-1], sell[-1], 0)
