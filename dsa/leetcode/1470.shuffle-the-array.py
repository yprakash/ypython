# @author: yprakash
from functools import reduce
from typing import List


class Solution:
    # https://leetcode.com/problems/shuffle-the-array/submissions/892743939/
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [a for x, y in zip(nums, nums[n:]) for a in (x, y)]

    # https://leetcode.com/submissions/detail/704885972/
    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])

    # https://leetcode.com/submissions/detail/704892639/
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
