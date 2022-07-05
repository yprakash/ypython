# INCOMPLETE
# @author: yprakash
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value in O(log n) runtime complexity.

from bisect import bisect_left, bisect_right


class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return [-1, -1]

        return [-1, -1]

    # https://leetcode.com/submissions/detail/731536573/
    # Using inbuilt bisect methods
    def searchRange2(self, nums, target):
        if nums:
            index = bisect_left(nums, target)
            if index < len(nums) and nums[index] == target:
                return [index, bisect_right(nums, target)-1]
        return [-1, -1]
