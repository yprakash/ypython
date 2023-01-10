# @author: yprakash
import heapq
import math
from typing import List


# https://leetcode.com/contest/weekly-contest-327/submissions/detail/873741108/
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k):
            n = heapq.heappop(nums)
            score -= n
            heapq.heappush(nums, -math.ceil(-n / 3))

        return score
