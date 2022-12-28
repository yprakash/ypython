# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-318/submissions/detail/837751164/
    def applyOperations(self, nums: List[int]) -> List[int]:
        k = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] > 0:
                nums[k] = nums[i]
                k += 1

        nums[k] = nums[-1]
        k += 1
        while k < len(nums):
            nums[k] = 0
            k += 1

        return nums
