# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/742327563/
    def canJump(self, nums):
        if len(nums) < 2:
            return True
        max_steps = 0

        for i, n in enumerate(nums[:len(nums)-1]):
            if n == 0 and max_steps <= i:
                return False
            if max_steps < i + n:
                max_steps = i + n
        return True


obj = Solution()
arr = [
    [0],  # True
    [0, 1],  # False
    [2, 0, 0],  # True
    [2, 3, 1, 1, 4],  # True
    [3, 2, 1, 0, 4]  # False
]
for a in arr:
    print(obj.canJump(a))
