# @author: yprakash
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value in O(log n) runtime complexity.

from bisect import bisect_left, bisect_right


class Solution(object):
    def search_left(self, nums, target, left, right):
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid - 1
            else:  # nums[mid] must have been lesser than target
                left = mid + 1
        return left

    def search_right(self, nums, target, left, right):
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left = mid + 1
            else:  # nums[mid] must have been greater than target
                right = mid - 1
        return right

    # https://leetcode.com/submissions/detail/739877885/
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)-1
        mid = -1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left > right:
            return [-1, -1]

        start = self.search_left(nums, target, 0, mid-1)
        end = self.search_right(nums, target, mid+1, len(nums)-1)
        return [start, end]

    # https://leetcode.com/submissions/detail/731536573/
    # Using inbuilt bisect methods
    def searchRange2(self, nums, target):
        if nums:
            index = bisect_left(nums, target)
            if index < len(nums) and nums[index] == target:
                return [index, bisect_right(nums, target)-1]
        return [-1, -1]


obj = Solution()
nums2d = [  # format: [target, [nums]]
    [0, []],
    [8, [5, 7, 7, 8, 8, 10]],
    [6, [5, 7, 7, 8, 8, 10]],
    [5, [1, 3, 3, 5, 5, 5, 8, 9]],
    [5, [1, 3, 3, 5, 5, 5, 5, 9]]
]
for arr in nums2d:
    print('target: ' + str(arr[0]) + ' & ' + str(arr[1]))
    print('LogN  : ' + str(obj.searchRange(arr[1], arr[0])))
    print('bisect: ' + str(obj.searchRange2(arr[1], arr[0])))
