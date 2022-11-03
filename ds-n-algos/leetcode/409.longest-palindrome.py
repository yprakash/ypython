# @author: yprakash
from collections import Counter


class Solution:
    # https://leetcode.com/submissions/detail/835750507/
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        odd = False
        counts = Counter(s)

        for char, freq in counts.items():
            if freq % 2 == 0:
                ans += freq
            else:
                odd = True
                ans += freq - 1

        if odd:
            ans += 1
        return ans
