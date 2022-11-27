# @author: yprakash
import math


class Solution:
    # Naive TLE: https://leetcode.com/submissions/detail/850467071/
    def bulbSwitch1(self, n: int) -> int:
        bulbs = [True] * (n + 1)
        bulbs[0] = False

        for step in range(2, n+1):
            for i in range(step, n+1, step):
                bulbs[i] = not bulbs[i]

        return sum(bulbs)

    # https://leetcode.com/submissions/detail/850487397/
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
