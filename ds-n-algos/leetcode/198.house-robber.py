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
