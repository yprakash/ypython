# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-320/submissions/detail/846626563/
    def unequalTriplets(self, nums: List[int]) -> int:
        n, count = len(nums), 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1

        return count
