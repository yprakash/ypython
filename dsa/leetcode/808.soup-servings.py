# @author: yprakash
from functools import cache


# https://leetcode.com/problems/soup-servings/submissions/1007740175/
# RecursionError: maximum recursion depth exceeded
class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def serve(a, b):
            if a <= 0:
                return 1 if b > 0 else 0.5
            if b <= 0:
                return 0

            return 0.25 * (
                serve(a - 100, b) +
                serve(a - 75, b - 25) +
                serve(a - 50, b - 50) +
                serve(a - 25, b - 75)
            )

        return serve(n, n)
