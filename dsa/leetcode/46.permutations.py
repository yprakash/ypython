# @author: yprakash
from itertools import permutations
from typing import List


class Solution:
    # https://leetcode.com/problems/permutations/submissions/1009819873/
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)
