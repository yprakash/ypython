# @author: yprakash
from typing import List


# https://leetcode.com/problems/maximum-ice-cream-bars/submissions/872763516/
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = 0
        costs.sort()

        for c in costs:
            if coins < c:
                return n

            coins -= c
            n += 1
        return n
