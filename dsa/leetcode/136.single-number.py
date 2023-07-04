# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/problems/single-number/submissions/986392892/
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num
        return n
