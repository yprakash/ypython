# @author: yprakash
from functools import reduce
from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda i, j: i ^ j, nums)
