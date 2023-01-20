# @author: yprakash
# TC: O(2^n * n), 2^n to explore all possible states, and n comes from changing the subsequence from list to tuple.
from typing import List


# https://leetcode.com/problems/non-decreasing-subsequences/submissions/881547515/
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, sequence):
            nonlocal res
            if len(sequence) > 1:
                res.add(tuple(sequence))
            if i >= len(nums):
                return

            if not sequence or sequence[-1] <= nums[i]:
                backtrack(i+1, sequence + [nums[i]])
            backtrack(i+1, sequence)

        res = set()
        backtrack(0, [])
        return res
