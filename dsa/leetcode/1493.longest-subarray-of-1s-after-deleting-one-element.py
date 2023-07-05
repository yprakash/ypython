# @author: yprakash
from functools import cache
from typing import List


class Solution:
    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/986601357/
    def longestSubarray(self, nums: List[int]) -> int:
        @cache
        def longest(curr_index, removed_any_till_now, prev_max):
            if curr_index >= len(nums):
                return prev_max

            if nums[curr_index] == 1:
                return longest(curr_index + 1, removed_any_till_now, prev_max + 1)
            else:
                if removed_any_till_now:  # already one element removed previously
                    return max(prev_max, longest(curr_index + 1, 1, 0))
                return max(
                    longest(curr_index + 1, 1, prev_max),  # remove current element
                    longest(curr_index + 1, 0, 0)  # without removing current element
                )

        long = longest(0, 0, 0)
        if long == len(nums):
            return long - 1
        return long
