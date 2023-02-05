# @author: yprakash
from collections import Counter


# https://leetcode.com/problems/permutation-in-string/submissions/892064257/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        s2c = Counter(s2[:len(s1) - 1])

        for x, y in zip(s2, s2[len(s1) - 1:]):
            if y in s2c:
                s2c[y] += 1
            else:
                s2c[y] = 1
            if s1c == s2c:
                return True
            s2c[x] -= 1
            if s2c[x] == 0:
                del s2c[x]

        return False
