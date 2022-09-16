# @author: yprakash
from functools import lru_cache
from typing import List


class Solution(object):
    # https://leetcode.com/submissions/detail/801431641/
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(maxsize=2000)
        def max_score(index, left, right):
            if index == len(multipliers):
                return 0
            return max(
                multipliers[index] * nums[left] + max_score(index+1, left+1, right),
                multipliers[index] * nums[right] + max_score(index+1, left, right-1)
            )

        return max_score(0, 0, len(nums)-1)


if __name__ == "__main__":
    testcases = [
        [[1, 2, 3], [3, 2, 1]],  # 14
        [[-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]],  # 102
    ]
    obj = Solution()
    for n, m in testcases:
        print(obj.maximumScore(n, m))
