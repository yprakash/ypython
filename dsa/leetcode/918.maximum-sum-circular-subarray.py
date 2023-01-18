# @author: yprakash
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_so_far = nums[0]
        curr_min = nums[0]
        min_so_far = nums[0]
        arr_sum = sum(nums)

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)
            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)

        if min_so_far == arr_sum:
            return max_so_far
        return max(max_so_far, arr_sum - min_so_far)
