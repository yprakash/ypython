# @author: yprakash
from functools import lru_cache
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/827901394/
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def non_adjacent_max_sum(index):
            if index >= len(nums):
                return 0

            return max(non_adjacent_max_sum(index+1),
                       nums[index] + non_adjacent_max_sum(index+2))

        return non_adjacent_max_sum(0)

    # https://leetcode.com/submissions/detail/838901586/
    # Bottom-up Tabulation
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
