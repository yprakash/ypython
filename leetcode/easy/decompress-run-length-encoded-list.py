# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    # https://leetcode.com/submissions/detail/706396330/
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        i = 0
        while i < n:
            res += [nums[i + 1]] * nums[i]
            i += 2
        return res

    # https://leetcode.com/submissions/detail/706383830/
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return reduce(lambda a, b: a + b, [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)])