# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-321/submissions/detail/850438817/
    # Naive O(N^2) TLE
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        answer = 0
        inr = [0, 1]
        ki = nums.index(k)

        for si in range(ki, -1, -1):  # start index of subarray
            lesser, greater = 0, 0
            for ei in range(si, len(nums)):
                if nums[ei] <= k:
                    lesser += 1
                else:
                    greater += 1
                if ei >= ki and lesser - greater in inr:
                    answer += 1

        return answer
