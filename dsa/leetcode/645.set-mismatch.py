# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/828304068/
    def findErrorNums(self, nums: List[int]) -> List[int]:
        int_map = {}
        repeating, missing = 0, 0

        for n in nums:
            if n in int_map:
                repeating = n
            else:
                int_map[n] = True

        for n in range(1, 1+len(nums)):
            if n not in int_map:
                return [repeating, n]

        return [repeating, n]  # Shouldn't occur
