# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/854428272/
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        p, x = 0, skill[0] + skill[-1]
        l, r = 0, len(skill) - 1  # left, right pointers

        while l < r:
            if skill[l] + skill[r] != x:
                return -1
            p += skill[l] * skill[r]
            l += 1
            r -= 1

        return p
