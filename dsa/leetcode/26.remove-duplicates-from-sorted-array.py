# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/841093442/
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i + 1 < len(nums):
            if nums[i] < nums[i + 1]:
                i += 1
            else:
                del nums[i + 1]

        return len(nums)
