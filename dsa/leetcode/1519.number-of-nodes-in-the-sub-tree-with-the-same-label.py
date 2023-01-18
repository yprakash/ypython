# @author: yprakash
from collections import defaultdict, Counter
from typing import List


# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/submissions/876903987/
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)

        res = [0] * n

        def dfs(node, par):
            nonlocal res
            count = Counter()
            for nei in tree[node]:
                if nei != par:
                    count += dfs(nei, node)

            count[labels[node]] += 1
            res[node] = count[labels[node]]

            return count

        dfs(0, -1)
        return res
