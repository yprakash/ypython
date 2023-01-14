# @author: yprakash
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/submissions/877796890/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(a, b)

        return ''.join([find(a) for a in baseStr])
