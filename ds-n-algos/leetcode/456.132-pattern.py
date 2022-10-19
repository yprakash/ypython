# @author: yprakash
import math
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/825988836/
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        smallest = math.inf

        for num in nums:
            while stack and stack[-1][1] <= num:
                stack.pop()
            if stack and stack[-1][0] < num:
                return True

            stack.append((smallest, num))
            smallest = min(smallest, num)

        return False
