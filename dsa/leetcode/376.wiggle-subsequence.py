# @author: yprakash

class Solution(object):
    def wiggleMaxLength(self, nums):
        peaks = 1
        valleys = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                peaks = valleys + 1
            elif nums[i] < nums[i-1]:
                valleys = peaks + 1
        return max(peaks, valleys)
