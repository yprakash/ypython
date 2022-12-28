# @author: yprakash
from collections import Counter


class Solution(object):
    # https://leetcode.com/submissions/detail/774778069/
    def firstUniqChar(self, s):
        dct = Counter(s)
        for i, c in enumerate(s):
            if dct[c] == 1:
                return i
        return -1
