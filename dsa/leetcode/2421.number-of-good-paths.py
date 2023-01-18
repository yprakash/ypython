# author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/number-of-good-paths/submissions/878595112/
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)
        if aroot == broot:
            return False

        if self.rank[aroot] < self.rank[broot]:
            self.parent[aroot] = broot
            self.rank[broot] += self.rank[aroot]
        else:
            self.parent[broot] = aroot
            self.rank[aroot] += self.rank[broot]
        return True


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        val_to_index = defaultdict(list)
        for i, v in enumerate(vals):
            val_to_index[v].append(i)

        answer = 0
        uf = UnionFind(len(vals))
        for val in sorted(val_to_index.keys()):
            for i in val_to_index[val]:
                for nei in graph[i]:
                    if vals[nei] <= vals[i]:
                        uf.union(nei, i)

            count = defaultdict(int)
            for i in val_to_index[val]:
                count[uf.find(i)] += 1
                answer += count[uf.find(i)]

        return answer
