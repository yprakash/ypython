# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/854355968/
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums or n < 2:
            return 0

        left, right = nums[0], sum(nums) - nums[0]
        diff = abs(left - int(right / (n - 1)))
        index = 0

        for i in range(1, n - 1):
            left += nums[i]
            right -= nums[i]
            tmp = abs(int(left / (i + 1)) - int(right / (n - i - 1)))
            if tmp < diff:
                index = i
                diff = tmp

        left += nums[-1]
        tmp = int(left / n)
        if tmp < diff:
            index = n - 1

        return index
