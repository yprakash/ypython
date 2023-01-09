# @author: yprakash
from typing import List


# https://leetcode.com/problems/gas-station/submissions/873314185/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = idx = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                tank, idx = 0, i + 1

        return idx
