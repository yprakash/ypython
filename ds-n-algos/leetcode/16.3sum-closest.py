# @author: yprakash
import math
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/834049482/
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, distance = 0, math.inf

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == target:
                    return sum3

                if distance > abs(target - sum3):
                    ans = sum3
                    distance = abs(target - ans)

                if sum3 < target:
                    left += 1
                else:
                    right -= 1

        return ans
