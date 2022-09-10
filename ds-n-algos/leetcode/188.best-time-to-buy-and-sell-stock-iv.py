# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/796296049/
    def maxProfit(self, k, prices):
        if k <= 0 or len(prices) < 2:
            return 0
        profit = [[0] * len(prices) for _ in range(k+1)]

        for i in range(1, k+1):
            ebp = prices[0]
            for j in range(1, len(prices)):
                profit[i][j] = max(profit[i][j-1], prices[j] - ebp)
                ebp = min(ebp, prices[j] - profit[i-1][j])

        return profit[k][-1]

    # https://leetcode.com/submissions/detail/796284699/
    # O(k * n^2) DP approach: Time Limit Exceeded
    def maxProfit3(self, k, prices):
        if k <= 0 or len(prices) < 2:
            return 0
        profit = [[0] * len(prices) for _ in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, len(prices)):
                profit[i][j] = max(profit[i][j-1],  # NO transaction on j-th day
                                   max([profit[i-1][x] + prices[j] - prices[x] for x in range(j)]))

        return profit[k][-1]


if __name__ == "__main__":
    testcases = [
        [2, []],  # 0
        [2, [2, 4, 1]],  # 2
        [2, [3, 2, 6, 5, 0, 3]],  # 7
        [3, [3, 2, 6, 5, 0, 3, 2, 6]]  # 11
    ]
    for k, price in testcases:
        obj = Solution()
        print(obj.maxProfit(k, price))
