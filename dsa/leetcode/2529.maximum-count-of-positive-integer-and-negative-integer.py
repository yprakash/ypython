# @author: yprakash
from typing import List


# https://leetcode.com/contest/weekly-contest-327/submissions/detail/873729642/
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for n in nums:
            if n < 0:
                neg += 1
            elif n > 0:
                pos += 1
        return max(pos, neg)
