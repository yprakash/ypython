# @author: yprakash
import math
from typing import List


class Solution(object):
    # https://leetcode.com/submissions/detail/840553012/
    # O(1) space & O(N) Time
    def maxProfit(self, prices: List[int]) -> int:
        profit1, profit2 = 0, 0
        buy_price1, buy_price2 = math.inf, math.inf

        for curr_price in prices:
            buy_price1 = min(buy_price1, curr_price)
            profit1 = max(profit1, curr_price - buy_price1)
            buy_price2 = min(buy_price2, curr_price - profit1)
            profit2 = max(profit2, curr_price - buy_price2)

        return profit2

    # DP based on the recurrence relation from Naive approach
    # https://leetcode.com/submissions/detail/796227422/
    # O(N) space & Time
    def maxProfit(self, prices):
        profit = 0
        min_till_now = prices[0]
        left_max = [0] * len(prices)
        for i, price in enumerate(prices):
            min_till_now = min(min_till_now, price)
            profit = max(profit, price - min_till_now)
            left_max[i] = profit

        profit = 0
        max_till_now = prices[-1]
        right_max = [0] * len(prices)
        for i, price in reversed(list(enumerate(prices))):
            max_till_now = max(max_till_now, price)
            profit = max(profit, max_till_now - price)
            right_max[i] = profit

        max_till_now = right_max[0]
        for i in range(1, len(prices)):
            max_till_now = max(max_till_now, left_max[i-1]+right_max[i])
        return max_till_now

    # For every index i, calculate single_max_profit from 0 to (i-1) and i to n-1
    # https://leetcode.com/submissions/detail/796202937/
    # O(N^2) Naive Approach: Time Limit Exceeded
    def maxProfit3(self, prices):
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, self.single_max_profit(prices, 0, i) + self.single_max_profit(prices, i, len(prices)))
        return profit

    def single_max_profit(self, prices, start, end):
        profit = 0
        min_till_now = prices[start]

        for price in prices[start:end]:
            if min_till_now >= price:
                min_till_now = price
            elif profit < price - min_till_now:
                profit = price - min_till_now
        return profit


if __name__ == "__main__":
    testcases = [
        [1, 2, 3, 4, 5],  # 4
        [7, 6, 4, 3, 1],  # 0
        [7, 1, 5, 3, 6, 4],  # 4 + 3
        [3, 3, 5, 0, 0, 3, 1, 4],  # 6
        [1, 2, 4, 2, 5, 7, 2, 4, 9, 0],  # 13
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.maxProfit(testcase))
