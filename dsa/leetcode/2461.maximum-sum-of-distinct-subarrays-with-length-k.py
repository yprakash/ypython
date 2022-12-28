# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/contest/weekly-contest-318/submissions/detail/837773922/
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return max(nums)

        i, ksum = 0, 0
        j, tmp = 1, nums[0]
        s = set()
        s.add(nums[0])

        while i <= len(nums) - k:
            distinct = True

            for j in range(j, i+k):
                if nums[j] in s:
                    distinct = False
                    break
                tmp += nums[j]
                s.add(nums[j])

            if distinct:
                ksum = max(ksum, tmp)
                s.remove(nums[i])
                tmp -= nums[i]
                i += 1
            else:
                i = j
                tmp = nums[i]
                s = set()
                s.add(nums[i])

            j += 1

        return ksum
