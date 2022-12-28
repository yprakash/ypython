# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/809022793/
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]

        def ufind(x):
            return x if x == parent[x] else ufind(parent[x])

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            parent[ua] = ub

        for equation in equations:
            if equation[1] == '!':
                continue

            x = ord(equation[0]) - ord('a')
            y = ord(equation[3]) - ord('a')
            uunion(x, y)

        for equation in equations:
            if equation[1] != '!':
                continue

            x = ord(equation[0]) - ord('a')
            y = ord(equation[3]) - ord('a')

            if ufind(x) == ufind(y):
                return False

        return True
