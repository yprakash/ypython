# @author: yprakash
from itertools import accumulate
from typing import List


# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/submissions/913519657/
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums = [n for n in accumulate(nums) if n > 0]
        return len(nums)
