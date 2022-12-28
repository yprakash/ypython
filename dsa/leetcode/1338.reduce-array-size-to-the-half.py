# @author: yprakash
from collections import Counter


class Solution(object):
    # https://leetcode.com/submissions/detail/776548126/
    def minSetSize(self, arr):
        mn = 0
        size = len(arr)
        counter = Counter(arr)

        for e, f in counter.most_common():
            mn += 1
            size -= f
            if size <= len(arr) / 2:
                return mn

        return None
