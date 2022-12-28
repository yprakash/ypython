# @author: yprakash
from typing import List


class Solution(object):
    # https://leetcode.com/submissions/detail/769396396/
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans = 0
        mod = 7 + 10 ** 9
        arr.sort()
        dp = {}

        for i, num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0 and num / arr[j] in dp:
                    dp[num] = (dp[num] + dp[arr[j]] * dp[num / arr[j]]) % mod

            ans = (ans + dp[num]) % mod

        return ans
