# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/784797028/
    # Using (slight variation of) Kadane's algorithm
    def maxSubArray(self, nums):
        curr_max = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            if max_so_far < curr_max:
                max_so_far = curr_max

        return max_so_far
