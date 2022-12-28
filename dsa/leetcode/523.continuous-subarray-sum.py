# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/830317295/
    # Correct but Naive O(N*2), Time Limit Exceeded
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        prefix_sum = [0] * (1 + len(nums))
        for i, num in enumerate(nums, 1):
            prefix_sum[i] = num + prefix_sum[i-1]

        for i in range(1, len(nums)):
            for j in range(i):
                if (prefix_sum[i+1] - prefix_sum[j]) % k == 0:
                    return True

        return False

    # https://leetcode.com/problems/continuous-subarray-sum/discuss/2744281/C%2B%2B-or-PYTHON-oror-EXPLAINED-oror
    # https://leetcode.com/submissions/detail/830331692/
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s, sum_index = 0, {0: -1}
        for i, num in enumerate(nums):
            s = (s + num) % k  # 1 <= k <= 2^31 - 1 from Constraint
            if s not in sum_index:
                sum_index[s] = i
            elif i - sum_index[s] >= 2:
                return True

        return False
