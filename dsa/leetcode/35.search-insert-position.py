# @author: yprakash
import bisect
from typing import List


# https://leetcode.com/problems/search-insert-position/submissions/901300772/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
