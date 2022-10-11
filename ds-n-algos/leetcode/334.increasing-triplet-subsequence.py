# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/820228968/
    def increasingTriplet(self, nums: List[int]) -> bool:
        mn, mx = 0, len(nums) - 1
        # smaller[i] stores the index of a number which is smaller than arr[i] and is on the left side.
        smaller = [-1] * len(nums)

        for i in range(1, len(nums)):
            if nums[mn] < nums[i]:
                smaller[i] = mn
            else:
                mn = i

        # greater[i] stores the index of a number which is greater than arr[i] and is on the right side of arr[i]
        greater = [-1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[mx]:
                greater[i] = mx
            else:
                mx = i

        for i in range(len(nums)):
            if smaller[i] != -1 and greater[i] != -1:
                return True
        return False


if __name__ == "__main__":
    testcases = [
        [1, 2, 3, 4, 5],  # True
        [5, 4, 3, 2, 1],  # False
        [2, 1, 5, 0, 4, 6],  # True
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.increasingTriplet(testcase))
