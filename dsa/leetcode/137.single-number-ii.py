# @author: yprakash
import collections
from typing import List


class Solution:
    # https://leetcode.com/problems/single-number-ii/submissions/986225591/
    # TCSC: O(N)
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        for num, count in freq.items():
            if count == 1:
                return num
        return num
