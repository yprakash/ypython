# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739351034/
    def maxProfit(self, prices):
        profit = 0
        min_till_now = prices[0]

        for price in prices:
            if min_till_now >= price:
                min_till_now = price
            elif profit < price - min_till_now:
                profit = price - min_till_now
        return profit
