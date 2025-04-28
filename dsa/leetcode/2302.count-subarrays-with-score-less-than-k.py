# @author: yprakash
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/submissions/1619912196
from itertools import accumulate
from typing import List


class Solution2:
    # INCOMPLETE
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        l, s = 0, 0
        ps = []
        for num in nums:
            l += 1
            s += num
            ps.append(l * s) """

        def acc(state, num):
            prev_sum, prev_len = state
            return (prev_sum + num, prev_len + 1)

        ps2 = list(accumulate(nums, lambda state, num: acc(state, num), initial=(0, 0)))
        # More efficient way to calculate ps is above without acc, funciton calling
        ps = [s * l for s, l in ps2[1:]]

        count, n = 0, len(nums)
        score, l = 1, 0
        for r, n in enumerate(ps):
            score *= n
            while l <= r:
                score /= nums[l]
                if score < k:
                    break
                count += r - 1

        return count

# Editorial
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res, total = 0, 0
        i = 0
        for j in range(n):
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res
