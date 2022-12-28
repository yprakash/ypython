# @author: yprakash
from functools import cache
from typing import List


class Solution(object):
    def combinationSum4(self, nums, target):
        # https://leetcode.com/submissions/detail/766098830/
        # bottom-up DP approach
        dp = {0: 1}
        for total in range(1, target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n, 0)

        return dp[target]

    # https://leetcode.com/submissions/detail/766119875/
    # Cached recursive approach (top-down). Should be python3 to use @cache
    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        @cache
        def combination_sum(target2):
            if target2 < 0:
                return 0
            if target2 == 0:
                return 1
            count = 0

            for n in nums:
                count += combination_sum(target2 - n)
            return count

        return combination_sum(target)
