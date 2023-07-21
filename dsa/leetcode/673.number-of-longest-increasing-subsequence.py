# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/problems/number-of-longest-increasing-subsequence/submissions/1000099271/
    def findNumberOfLIS(self, nums: List[int]) -> int:
        counts = [1] * len(nums)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            # dp[i] = max(dp[i], max((1 + dp[j] for j in range(i) if nums[j] < nums[i]), default=0))
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        counts[i] = counts[j]
                    elif dp[i] == 1 + dp[j]:
                        counts[i] += counts[j]

        longest_len = max(dp)
        return sum([counts[i] for i in range(len(nums)) if dp[i] == longest_len])


if __name__ == "__main__":
    testcases = [
        [1, 3, 5, 4, 7],  # 2
        [2, 2, 2, 2, 2],  # 5
        [1, 2, 4, 3, 5, 4, 7, 2],  # 3
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.findNumberOfLIS(testcase))
