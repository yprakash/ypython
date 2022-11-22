# @author: yprakash
from math import sqrt


class Solution:
    # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    # https://leetcode.com/submissions/detail/847777275/
    def numSquares(self, n):
        if int(sqrt(n)) ** 2 == n:
            return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j * j)) ** 2 == n - j * j:
                return 2

        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        return 3
