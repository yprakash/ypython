# https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter


class Solution:
    # https://leetcode.com/submissions/detail/704934799/
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([int(nums[i] == nums[j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums))])

    # https://leetcode.com/submissions/detail/704938781/
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        dct = {}
        for n in nums:
            if n in dct:
                res += dct[n]
                dct[n] += 1
            else:
                dct[n] = 1
        return res

    # https://leetcode.com/submissions/detail/704949552/
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return int(sum(map(lambda x: x * (x - 1) / 2, Counter(nums).values())))
