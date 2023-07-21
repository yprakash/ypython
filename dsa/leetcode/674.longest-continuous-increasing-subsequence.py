# @author: yprakash
from typing import List


# https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/999920007/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_lcis, max_lcis = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_lcis += 1
            else:
                max_lcis = max(max_lcis, curr_lcis)
                curr_lcis = 1

        return max(max_lcis, curr_lcis)
