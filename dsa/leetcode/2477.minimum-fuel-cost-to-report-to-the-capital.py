# @author: yprakash
import math
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/submissions/897237447/
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        tree = defaultdict(set)
        for u, v in roads:
            tree[u].add(v)
            tree[v].add(u)

        def fuel_cost(node):
            cost, tn = 0, 1
            for v in tree[node]:
                tree[v].remove(node)
            if not tree[node]:
                return 1, 1

            for v in tree[node]:
                c, n = fuel_cost(v)
                cost += c
                tn += n
            return cost + math.ceil(tn / seats), tn

        c, n = fuel_cost(0)
        c -= math.ceil(n / seats)
        return c
