# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/796054674/
    def maxProfit(self, prices):
        profit, curr_profit = 0, 0
        curr_min = prices[0]

        for price in prices:
            if curr_profit < price - curr_min:
                curr_profit = price - curr_min
            else:
                curr_min = price
                if curr_profit > 0:  # not needed
                    profit += curr_profit
                    curr_profit = 0

        profit += curr_profit
        return profit


if __name__ == "__main__":
    testcases = [
        [1, 2, 3, 4, 5],  # 4
        [7, 6, 4, 3, 1],  # 0
        [7, 1, 5, 3, 6, 4],  # 4 + 3
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.maxProfit(testcase))
