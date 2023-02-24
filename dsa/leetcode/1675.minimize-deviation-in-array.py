# @author: yprakash
import heapq
from typing import List


# https://leetcode.com/problems/minimize-deviation-in-array/submissions/903880544/
# TC: O(N logN), SC: O(1)
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        deviation = max(nums) - min(nums)
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                nums[i] = -nums[i]
            else:
                nums[i] = -(nums[i] * 2)

        heapq.heapify(nums)
        mn = -max(nums)

        while nums:
            elem = -heapq.heappop(nums)
            deviation = min(deviation, elem - mn)
            if elem & 1 == 1:
                break
            elem >>= 1
            mn = min(mn, elem)
            heapq.heappush(nums, -elem)

        return deviation
