# @author: yprakash
from typing import List


# https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/901959886/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        left, mid = 0, 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                return nums[mid]
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or \
                    (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid - 1

        return -1
