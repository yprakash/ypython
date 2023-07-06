# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-size-subarray-sum/submissions/987428645/
    # Sliding Window O(N)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        left, sub_sum = 0, 0

        for right in range(len(nums)):
            sub_sum += nums[right]
            while sub_sum >= target:
                sub_sum -= nums[left]
                min_len = min(min_len, 1 + right - left)
                left += 1

        return 0 if min_len > len(nums) else min_len
