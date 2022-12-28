# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/826998262/
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}

        for i, num in enumerate(nums):
            if num in table and i - table[num] <= k:
                return True
            table[num] = i

        return False
