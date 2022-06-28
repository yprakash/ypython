# @author: yprakash

from collections import Counter


class Solution(object):
    # https://leetcode.com/submissions/detail/733113592/
    def minDeletions(self, s):
        dels = 0  # No.of deletions
        cntr = Counter(s)
        used = set()

        for key, value in cntr.items():
            while value and value in used:
                value -= 1
                dels += 1
            used.add(value)

        return dels
