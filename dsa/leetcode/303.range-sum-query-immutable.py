# @author: yprakash

class NumArray(object):
    def __init__(self, nums):
        self.prefix_sum = [0] * (1 + len(nums))
        for i, num in enumerate(nums, 1):
            self.prefix_sum[i] = num + self.prefix_sum[i-1]

    # https://leetcode.com/submissions/detail/754716061/
    def sumRange(self, left, right):
        return self.prefix_sum[1+right] - self.prefix_sum[left]
