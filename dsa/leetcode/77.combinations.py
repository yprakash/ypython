# @author: yprakash
from itertools import combinations
from typing import List


# https://leetcode.com/problems/combinations/submissions/1008969140/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1, 1 + n), k)
