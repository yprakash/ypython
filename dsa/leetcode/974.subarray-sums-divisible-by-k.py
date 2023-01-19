# @author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/880882496/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans, rem, sub_sum = 0, 0, 0
        freq = defaultdict(int)
        freq[0] = 1

        for i in range(len(nums)):
            sub_sum += nums[i]
            rem = sub_sum % k
            if rem < 0:
                rem += k
            ans += freq[rem]
            freq[rem] += 1

        return ans
