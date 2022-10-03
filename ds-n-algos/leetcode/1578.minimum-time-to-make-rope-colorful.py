# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/814117211/
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = list(colors)
        total_time = 0
        prev_char, prev_index = colors[0], 0
        for i, c in enumerate(colors[1:], 1):
            if c == prev_char:
                if neededTime[prev_index] < neededTime[i]:
                    total_time += neededTime[prev_index]
                    prev_char, prev_index = c, i
                else:
                    total_time += neededTime[i]
            else:
                prev_char, prev_index = c, i

        return total_time
