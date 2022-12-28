# @author: yprakash
import heapq
from typing import List


# https://leetcode.com/problems/remove-stones-to-minimize-the-total/submissions/866643981/
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)

        for i in range(k):
            x = -heapq.heappop(piles)
            x = x - x // 2
            heapq.heappush(piles, -x)

        return -sum(piles)
