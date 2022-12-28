# @author: yprakash
from typing import List


# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/submissions/866063350/
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer = 0
        need = [e1 - e2 for (e1, e2) in zip(capacity, rocks)]
        need.sort()

        for n in need:
            if additionalRocks < n:
                break
            answer += 1
            additionalRocks -= n

        return answer
