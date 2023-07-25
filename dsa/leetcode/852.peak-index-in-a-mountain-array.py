# @author: yprakash
from typing import List


# https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1003392115/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if arr[0] >= arr[1]:
            return 0
        if arr[-1] >= arr[-2]:
            return len(arr) - 1

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid-1] > arr[mid]:
                right = mid
            elif arr[mid] < arr[mid + 1]:
                left = mid
            else:
                return mid
        return left
