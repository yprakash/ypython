# @author: yprakash
# https://leetcode.com/problems/flip-string-to-monotone-increasing/submissions/880004236/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, flips = 0, 0
        for c in s:
            if c == '1':
                ones += 1
            elif ones:
                flips += 1
            flips = min(flips, ones)

        return flips
