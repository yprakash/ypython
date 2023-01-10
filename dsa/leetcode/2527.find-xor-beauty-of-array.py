# @author: yprakash
from functools import reduce
from typing import List


# https://leetcode.com/contest/biweekly-contest-95/submissions/detail/873416385/
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda i, j: i ^ j, nums)
