# @author: yprakash
from itertools import permutations


# https://leetcode.com/problems/shortest-string-that-contains-three-strings/submissions/1007592542/
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x, y):
            if y in x:
                return x
            res = 0
            for i in range(1, min(len(x), len(y))):
                if x[-i:] == y[:i]:
                    res = i
            return x + y[res:]

        ans = (float('inf'), "")
        for perm in permutations([a, b, c]):
            curr = ''
            for s in perm:
                curr = merge(curr, s)
            ans = min(ans, (len(curr), curr))

        return ans[1]
