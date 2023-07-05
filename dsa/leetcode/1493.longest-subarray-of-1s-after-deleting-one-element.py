# @author: yprakash
from functools import cache
from typing import List


class Solution:
    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/986601357/
    # DP memoization
    def longestSubarray1(self, nums: List[int]) -> int:
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

    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/987125836/
    # DP Tabulation
    def longestSubarray2(self, nums: List[int]) -> int:
        ans = nums[0]
        dp = [[0, 0] for i in range(len(nums))]
        dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 1:  #
                dp[i][0] = 1 + dp[i-1][0]
                dp[i][1] = 1 + dp[i-1][1]
            else:
                dp[i][0] = 0
                dp[i][1] = 1 + dp[i-1][0]

            ans = max(ans, dp[i][0], dp[i][1])

        return ans - 1

    # https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/987201799/
    # Calculate consecutive 1's to left and right side of every 0 and take max
    # Sliding Window technique
    def longestSubarray(self, nums: List[int]) -> int:
        left_sum, right_sum, best = 0, 0, 0
        for n in nums:
            if n:
                right_sum += 1
            else:
                best = max(best, left_sum + right_sum)
                left_sum = right_sum
                right_sum = 0

        best = max(best, left_sum + right_sum)
        return best if any(n == 0 for n in nums) else best - 1
