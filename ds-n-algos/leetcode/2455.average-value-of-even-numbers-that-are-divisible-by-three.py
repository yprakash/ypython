# @author: yprakash
# https://leetcode.com/contest/weekly-contest-317/submissions/detail/833051860/
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 6 == 0]
        return sum(nums) // len(nums) if nums else 0
