# @author: yprakash
import math
from typing import List


# https://leetcode.com/problems/jump-game-ii/submissions/893981386/
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [math.inf] * n
        jumps[0] = 0

        for i in range(n):
            for j in range(i+1, min(n, i+1+nums[i])):
                if 1 + jumps[i] < jumps[j]:
                    jumps[j] = 1 + jumps[i]

        return int(jumps[-1])
