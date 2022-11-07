# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/838571092/
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even = len(nums) - 1, len(nums) - 2

        for i, num in enumerate(nums):
            if i % 2 == 0:
                if num % 2 != 0:
                    while nums[odd] % 2 != 0:
                        odd -= 2
                    nums[i], nums[odd] = nums[odd], num
            else:
                if num % 2 == 0:
                    while nums[even] % 2 == 0:
                        even -= 2
                    nums[i], nums[even] = nums[even], num

        return nums
