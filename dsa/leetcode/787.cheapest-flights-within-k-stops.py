# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/885751127/
# TC: O(V + E*K) & SC: O(V + E)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, p in flights:
            adj[s].append((d, p))

        cost = [float('inf')] * n
        cost[src] = 0
        q = deque([(src, 0)])

        for _ in range(1 + k):
            for i in range(len(q)):
                city, price = q.popleft()
                for n, p in adj[city]:
                    if p + price < cost[n]:
                        cost[n] = p + price
                        q.append((n, cost[n]))

        return -1 if cost[dst] == float('inf') else cost[dst]
