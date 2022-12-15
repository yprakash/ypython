# @author: yprakash
from functools import cache


class Solution:
    # https://leetcode.com/problems/longest-common-subsequence/submissions/859939707/
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def longest(t1, t2):
            if t1 < 0 or t2 < 0:
                return 0
            if text1[t1] == text2[t2]:
                return 1 + longest(t1-1, t2-1)
            return max(longest(t1-1, t2), longest(t1, t2-1))

        return longest(len(text1) - 1, len(text2) - 1)
