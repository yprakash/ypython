# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739395235/
    def getMaximumGenerated(self, n):
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1

        for i in range(1, int((n+1)/2)):
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)


obj = Solution()
print(obj.getMaximumGenerated(0))  # 0
print(obj.getMaximumGenerated(1))  # 1
print(obj.getMaximumGenerated(2))  # 1
print(obj.getMaximumGenerated(3))  # 2
print(obj.getMaximumGenerated(7))  # 3
