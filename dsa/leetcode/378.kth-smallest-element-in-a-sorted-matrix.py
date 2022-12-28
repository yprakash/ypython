# author: yprakash
from typing import List


class Solution(object):
    # https://leetcode.com/submissions/detail/763422260/
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k-1]
